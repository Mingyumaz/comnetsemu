#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8

"""
About: Test core features implemented in ComNetsEmu
"""

import functools
import subprocess
import unittest

from comnetsemu.net import VNFManager, Containernet
from comnetsemu.node import DockerContainer, DockerHost
from mininet.topo import Topo
from mininet.node import OVSBridge

# Measurement error threshold
CPU_ERR_THR = 5  # %
MEM_ERR_THR = 50  # MB


def CLEANUP():
    subprocess.run(["ce", "-c"], check=True, stdout=subprocess.DEVNULL,
                   stderr=subprocess.DEVNULL)


class TestTopo(Topo):

    def build(self, n=2):
        switch = self.addSwitch('s1')
        for h in range(1, n+1):
            host = self.addHost('h%s' % h)
            self.addLink(switch, host)

#  TODO:  <02-08-19, Zuo> Add testcase for DockerHost #


class TestVNFManager(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        CLEANUP()
        dargs = {
            "dimage": "dev_test",
            "dcmd": "bash"
        }
        dhost_test = functools.partial(DockerHost, **dargs)

        cls.net = Containernet(
            topo=TestTopo(3),
            switch=OVSBridge,
            host=dhost_test,
            autoSetMacs=True, autoStaticArp=True
        )
        cls.net.start()
        cls.mgr = VNFManager(cls.net)

    @classmethod
    def tearDownClass(cls):
        cls.net.stop()
        cls.mgr.stop()
        CLEANUP()

    def test_ping(self):
        ret = self.net.pingAll()
        self.assertEqual(ret, 0.0)

    def test_container_crud(self):
        c1 = self.mgr.addContainer("c1", "h1", "dev_test", "/bin/bash")
        self.mgr.removeContainer(c1)

    def test_container_isolation(self):
        h1 = self.net.get("h1")
        h2 = self.net.get("h2")
        h3 = self.net.get("h3")

        # CPU and memory
        h1.updateCpuLimit(cpu_quota=10000)
        h1.updateMemoryLimit(mem_limit=10 * (1024**2))  # in bytes
        c1 = self.mgr.addContainer(
            "c1", "h1", "dev_test", "stress-ng -c 1 -m 1 --vm-bytes 300M")
        usages = self.mgr.monResourceStats(c1)
        cpu = sum(u[0] for u in usages) / len(usages)
        mem = sum(u[1] for u in usages) / len(usages)
        self.assertTrue(abs(cpu - 10.0) <= CPU_ERR_THR)
        self.assertTrue(abs(mem - 10.0) <= MEM_ERR_THR)
        self.mgr.removeContainer(c1)
        h1.updateCpuLimit(cpu_quota=-1)
        h1.updateMemoryLimit(mem_limit=100 * (1024**3))

        # Network
        for r in [h2, h3]:
            c1 = self.mgr.addContainer("c1", r, "dev_test", "iperf -s")
            ret = h1.cmd("iperf -c {} -u -b 10M -t 3".format(r.IP()))
            clt_bw = float(self.net._parseIperf(ret).split(" ")[0])
            self.assertTrue(clt_bw > 0.0)
            self.mgr.removeContainer(c1)
