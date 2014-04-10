# Reactors Submodule

This directory contains classes that define Pantera reactors.

```python
import pantera as pt

pr = pt.PanteraReactor()
```

There isn't a whole lot here, because most of the useful functionality
is not provided by the reactor, but the reactor network.
In Pantera, reactor networks are also called "configurations." (As in,
a specific, pre-defined configuration of reactors, inlets, outlets, etc.)

## Reactors vs. Configurations

Cantera defines Reactors and Reactor Networks separately. Reactors are
basically just source term generators for a set of ordinary differential equations.
By adding reactors (and inlets and outlets) to a reactor network, you are
changing the variables and equations.

The Reactor Network object, then, is an ordinary differential equation 
integrator. It owns a set of equations, variables, and right-hand sides,
and when you call the ```advance()``` or ```solve()``` method on it, 
it integrates those in time.

## Inheritance

Pantera reactors take advantage of Cantera's object-oriented code
to re-use and extend existing Cantera code. Pantera Reactor objects inherit 
all of the characteristics of Cantera Reactor objects, so that allows us 
to use our Pantera Reactor anywhere we can use a Cantera Reactor.

## Pantera Reactor Bases

Contains base classes that define common functionality
for all Pantera reactors (specifically, taking a dictionary
of reactor input parameters, and defining a problem setup
method that processes these input parameters.

#### Isothermal and Adiabatic Reactors

To make an adiabatic or isothermal reactor,
remember that a Pantera Reactor can do anything a 
Cantera Reactor can do. So with Cantera, we would 
make an isothermal reactor like this:

```python
import cantera as ct

g = ct.Solution('gri30.xml')
g.TPX = 898.15, ct.one_atm, "C2H6:1.0, O2:4.0"

cr = ct.Reactor(g,energy='off')
```

```python
import pantera as pt

g = pt.Solution('gri30.xml')
g.TPX = 898.15, pt.one_atm, "C2H6:1.0, O2:4.0"

pr = pt.PanteraReactor(g,energy='off')
```

Voila! [OOP](http://en.wikipedia.org/wiki/Object_oriented_programming)!

