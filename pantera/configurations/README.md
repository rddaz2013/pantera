# Configurations Submodule

This directory contains classes that define Pantera configurations.

Configurations are the Pantera equivalent of a Cantera ReactorNet. 
Configurations allow for the fact that the user will want to 
initialize their system the way they initialize reactors -
by inserting a gas and passing options - but want to solve their
system the way they solve a reactor network - with a simple
call to a solve() method.

You can extend the Pantera Configuration class to handle multiple reactors,
multiple inlets, multiple outlets, or whatever your situation is.
You just redefine the constructor to take whatever arguments you want, 
then properly intialize whatever reactors and flow devices you want.
When you call advance, or do anything else with your configuration/reactor network,
it will behave just like a regular reactor network.

## How to Use Configurations

We can treat them the same way we treat reactor networks. With Cantera:

```python
import cantera as ct

g = get_gas() # imaginary function returning a Solution object with TPX set
ctreactor = ct.Reactor(g)
ctnet = ct.ReactorNet([ctreactor])
ctnet.advance(0.01)
```

The Pantera Configuration class functions the exact same way, via inheritance:

```python
import pantera as pt

g = get_gas() # imaginary function returning a Solution object with TPX set
ptreactor = pt.PanteraReactor(g)
ptconfig = pt.Configuration([ptreactor])
ptconfig.advance(0.01)
```

Of course, configurations are designed to do 
much more than Cantera reactor networks. 
We'll cover some examples shortly.



## Piston Cylinder (PC) Configurations

Piston cylinder configurations consist of two gases,
one on either side of a flexible wall.

The gas on the left side is the contents of your 
piston cylinder system. THe gas on the right side is the  
environment.

The pressure difference dictates the volume change of the cylinder,
through an expansion coefficient K,

```
\frac{dV}{dt} = K A ( P_{left} - P_{right} )
```
[More about piston cylinder systems](PC.md)





