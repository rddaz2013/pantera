# The Pantera Library Layout

This readme describes the layout of the core source code of Pantera.

Pantera provides classes that interface with and extend Cantera classes.

Pantera also monkey-patches Cantera, modifying Cantera objects to provide
useful functionality and/or bring back some of the features of Cantera's 
Python interface that disappeared in the 2.0 to 2.1 transition.

Pantera Sub-Modules:
* Cantera Monkey-Patches - patches existing Cantera classes - for essential functionality ONLY!
* [Gases submodule](gases/README.md) - gas compositions, gas mixing, gas objects
* [Configurations submodule](configurations/README.md) - extends Cantera reactor networks to be more useful and flexible (plug flow reactors, packed bed reactors, ignition reactors, recycle reactors, etc.)
* [Reactors submodule](reactors/README.md) - extends Cantera reactors to be more useful (but most of the useful stuff is in the configurations)
* [Engineering submodule](engineering/README.md) - applied engineering problems solved with Cantera

## Cantera Monkey-Patches

There are a couple of monkey patches applied to Cantera. The two classes affected are:
* Cantera.Reactor
* Cantera.Solution

### Solution class Monkey-Patches

The Solution class is monkey-patched to more easily obtain mass and mole fractions
for particular species.

If you have a Solution (bascially a gas phase object) using the Cantera library, you can 
obtain mass and mole fractions using the somewhat clunky notation:

```python
speciesName = ['CH4','O2']
Xs = my_solution[speciesName].X
Ys = my_solution[speciesName].Y
```

This monkey-patch allows for the much more intuitive:

```python
speciesName = ['CH4','O2']
Xs = my_solution.mole_fraction( speciesName )
Ys = my_solution.mass_fraction( speciesName )
```

Works for single species names or for lists of species names.

### Reactor class Monkey-Patches

The Reactor class monkey-patches are actually provided in the PanteraReactors.py file in the 
reactors submodule. It is described here anyway, since it is still a monkey-patch.

In Cantera 2.0, you could access the state of a Cantera reactor
like this:

```python
# Cantera 2.0
r = Reactor(my_solution)
print r.temperature()
print r.pressure()
print r.moleFractions()
```

However, Cantera 2.1 created problems by doing away with this. 
Now, you can only access the temperature of the reactor.

What's worse, if you want to access the pressure and mole fractions
of a reactor, you need to use the contents, but Cantera 2.1 also 
did away with ways of accessing the contents of the reactor. You
used to be able to do this:

```python
# Cantera 2.0
r = Reactor(my_solution)
c = r._contents
T = c.temperature()
P = c.pressure()
X = c.moleFractions()
```

Again, Cantera 2.1 created problems by doing away with this.

These monkey-patches fix this. Now you can do this:

```python
r = Reactor(my_solution)
print r.T
print r.P
print r.X
print r.Y

c = r._contents
print c.T
print c.P
print c.X
print c.Y
```

Woo hoo!

## Gases submodule

Pantera defines several utility functions
for things like specification of composition,
conversion of formats, mixing of gases, and 
others.

```python
from pantera.gases import *

ready_to_ignite = MethaneAir(phi=0.5)
```

[Visit the gases README.md for details](pantera/gases/README.md)

## Reactors submodule

You can create Pantera reactor objects. These 
extend Cantera's Reactor classes.

You can create them once you import Pantera:

```python
from pantera import *

pr = PanteraReactor()
```

[Visit the reactors README.md for details](pantera/reactors/README.md)

## Engineering submodule

Cantera is very handy for everyday engineering calculations, with an emphasis on 
reaction engineering and reactor design. This submodule creates some 
objects and methods that assist in these kinds of calculations.

```python
from pantera import *

h = Heater()
```

