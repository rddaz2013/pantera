# Configurations Submodule

This directory contains classes that define Pantera configurations.

Configurations are the Pantera analog to Cantera reactor networks. 
In Pantera, reactor networks are also called "configurations." (As in,
a specific, pre-defined configuration of reactors, inlets, outlets, etc.)

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



## Piston Cylinder (PC) Reactors

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





