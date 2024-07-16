from p4utils.mininetlib.network_API import NetworkAPI

net = NetworkAPI()

net.setLogLevel('info')

#Switches
net.addP4Switch('s1', cli_input='s1-commands.txt')
net.setThriftPort('s1',9081)

# P4 files
net.setP4Source('s1','basic.p4')

#Hosts
net.addHost('h1')
net.addHost('h2')

#Links
net.addLink('h1','s1', port1=1, port2=1, addr1="00:00:0a:00:01:01", addr2="00:00:00:00:01:02")
net.addLink('h2','s1', port1=1, port2=2, addr1="00:00:0a:00:01:02", addr2="00:00:00:00:01:03")


# Links parameters
net.setBw('s1','h1', 10) # Mbps
net.setBw('s1','h2', 10)

# IPs for hosts
net.setIntfIp('h1','s1','10.0.1.10/24')
net.setIntfIp('h2','s1','10.0.1.20/24')
# IPs for switch
net.setIntfIp('s1','h1','10.0.1.2/24') # port 2 = s1-eth2
net.setIntfIp('s1','h2','10.0.1.3/24') # port 3 = s1-eth3


net.setDefaultRoute('h1', '10.0.1.2')
net.setDefaultRoute('h2', '10.0.1.3')

#net.mixed()
net.enablePcapDumpAll()
#net.enableLogAll()

net.enableCli()

#net.addTaskFile('tasks.txt')
net.startNetwork()