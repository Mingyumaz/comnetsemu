from p4utils.mininetlib.network_API import NetworkAPI

net = NetworkAPI()

net.setLogLevel('info')

#Switches
net.addP4Switch('s1', cli_input='s1-commands.txt')
net.setThriftPort('s1',9081)
net.addP4Switch('s2', cli_input='s2-commands.txt')
net.setThriftPort('s2',9082)

# P4 files
net.setP4Source('s1','basic.p4')
net.setP4Source('s2','basic.p4')

#Hosts
net.addHost('h1')
net.addHost('h2')
net.addHost('h3')
net.addHost('h4')

#Links
net.addLink('h1','s1', port1=1, port2=2, addr1="00:00:0a:00:01:01", addr2="00:00:00:00:01:02")
net.addLink('h2','s1', port1=1, port2=3, addr1="00:00:0a:00:01:02", addr2="00:00:00:00:01:03")

net.addLink('s1','s2', port1=1, port2=1, addr1="00:00:00:00:01:01", addr2="00:00:00:00:02:01")

net.addLink('h3','s2', port1=1, port2=2, addr1="00:00:0a:00:01:03", addr2="00:00:00:00:02:02")
net.addLink('h4','s2', port1=1, port2=3, addr1="00:00:0a:00:01:04", addr2="00:00:00:00:02:03")

# Links parameters
net.setBw('s1','h1', 10) # Mbps
net.setDelay('s1','h1', 10) # ms
net.setBw('s1','h2', 10)
net.setDelay('s1','h2', 10)

net.setBw('s2','s1', 20)

net.setBw('s2','h3', 10)
net.setDelay('s2','h3', 10)
net.setBw('s2','h4', 10)
net.setDelay('s2','h4', 10)


# IPs for hosts
net.setIntfIp('h1','s1','10.0.1.10/24')
net.setIntfIp('h2','s1','10.0.1.20/24')

net.setIntfIp('h3','s2','10.0.2.10/24')
net.setIntfIp('h4','s2','10.0.2.20/24')
# IPs for switch
net.setIntfIp('s1','h1','10.0.1.2/24') # port 2 = s1-eth2
net.setIntfIp('s1','h2','10.0.1.3/24') # port 3 = s1-eth3
net.setIntfIp('s2','h3','10.0.2.2/24')
net.setIntfIp('s2','h4','10.0.2.3/24')


net.setDefaultRoute('h1', '10.0.1.2')
net.setDefaultRoute('h2', '10.0.1.3')
net.setDefaultRoute('h3', '10.0.2.2')
net.setDefaultRoute('h4', '10.0.2.3')

#net.mixed()
net.enablePcapDumpAll()
#net.enableLogAll()

net.enableCli()

#net.addTaskFile('tasks.txt')
net.startNetwork()