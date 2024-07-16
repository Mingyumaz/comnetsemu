### Introduction ###

This demo shows how to implement a basic IP routers with static routing entries using P4, BMv2 and Mininet. 

The basic functionality of IP router is:

- determine the output port for packet based on destination IP (Longest Prefix Match)
- decrement TTL value for IP protocol
- update destination MAC address based on next-hop IP address
- update source MAC address according to output port

We have implemented the functionality of IP router as P4 program (router.p4). The program design is as follows:

- We have used V1Model of P4_16 composed of Ingress and Egress control pipelines
- For Ingress control pipeline there is one table defined:
  - **routing_table** - it determines the output port based on IPv4 LPM. When packet is matched the *ipv4_forward* action is invoked. It sets next-hop IP address in the routing_metadata, decrements IPv4 TTL and sets output port.


### Demo ###


<p align="center">
  <img src="images/Network.png" />
</p>

1. First of all you need to setup the environment on your Linux machine.

2. Run the Mininet topology.

`sudo python3 network.py`

4. In the Mininet console, check if ping between h1 and h2 works

`h1 ping h2`
or `h1 ping h3` etc.

5. Have a nice day!


## Reference

**[1]** Anagnostakis K G, Greenwald M B, Ryger R S. On the sensitivity of network simulation to topology[C]//Proceedings. 10th IEEE International Symposium on Modeling, Analysis and Simulation of Computer and Telecommunications Systems. IEEE, 2002: 117-126.