# Implementing a P4 Calculator

### Introduction ###

The objective of this tutorial is to implement a basic calculator using a custom protocol header written in P4. The header will contain an operation to perform and two operands. When a switch receives a calculator packet header, it will execute the operation on the operands, and return the result to the sender.


### Demo ###


<p align="center">
  <img src="images/Network.png" />
</p>

### Introduction ###

To implement the calculator, you will need to define a custom calculator header, and implement the switch logic to parse header, perform the requested operation, write the result in the header, and return the packet to the sender.

We will use the following header format:

```
             0                1                  2              3
      +----------------+----------------+----------------+---------------+
      |      P         |       4        |     Version    |     Op        |
      +----------------+----------------+----------------+---------------+
      |                              Operand A                           |
      +----------------+----------------+----------------+---------------+
      |                              Operand B                           |
      +----------------+----------------+----------------+---------------+
      |                              Result                              |
      +----------------+----------------+----------------+---------------+

```

-  P is an ASCII Letter 'P' (0x50)
-  4 is an ASCII Letter '4' (0x34)
-  Version is currently 0.1 (0x01)
-  Op is an operation to Perform:
 -   '+' (0x2b) Result = OperandA + OperandB
 -   '-' (0x2d) Result = OperandA - OperandB
 -   '&' (0x26) Result = OperandA & OperandB
 -   '|' (0x7c) Result = OperandA | OperandB
 -   '^' (0x5e) Result = OperandA ^ OperandB

We will assume that the calculator header is carried over Ethernet,
and we will use the Ethernet type 0x1234 to indicate the presence of
the header.

Given what you have learned so far, your task is to implement the P4
calculator program. There is no control plane logic, so you need only
worry about the data plane implementation.

A working calculator implementation will parse the custom headers,
execute the mathematical operation, write the result in the result
field, and return the packet to the sender.

### Test in ComNetsEmu ###

1. First of all you need to setup the environment on your Linux machine.

2. Run the Mininet topology.

`sudo python3 network_with_calc.py`

3. We've written a small Python-based driver program that will allow
you to test your calculator. You can run the driver program directly
from the Mininet command prompt:

```
mininet> h1 python3 calc.py
>
```

4. The driver program will provide a new prompt, at which you can type
basic expressions. The test harness will parse your expression, and
prepare a packet with the corresponding operator and operands. It will
then send a packet to the switch for evaluation. When the switch
returns the result of the computation, the test program will print the
result. However, because the calculator program is not implemented,
you should see an error message.


```
*** Starting CLI:
mininet> h1 python3 calc.py
> 1+2
The message send to switch is :  1+2
The result send back from server :  3
> 5*6
The message send to switch is :  5*6
Expected binary operator '-', '+', '&', '|', or '^'.
> 5|6
The message send to switch is :  5|6
The result send back from server :  7
> quit
mininet> exit
```

## Reference

The documentation for P4_16 and P4Runtime is available [here](https://p4.org/specs/)

All excercises in this repository use the v1model architecture, the documentation for which is available at:
1. The BMv2 Simple Switch target document accessible [here](https://github.com/p4lang/behavioral-model/blob/master/docs/simple_switch.md) talks mainly about the v1model architecture.
2. The include file `v1model.p4` has extensive comments and can be accessed [here](https://github.com/p4lang/p4c/blob/master/p4include/v1model.p4).
3. P4 Calculator [here](https://github.com/p4lang/tutorials/tree/master/exercises/calc)