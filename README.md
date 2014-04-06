pantera
=======

A toolbox for using and extending Cantera in Python.

## What is Cantera?

Cantera is an object-oriented toolkit for chemical kinetics.

It handles all sorts of thermochemistry stuff - everything from 
physical properties to reaction rates to reactors and ordinary 
differential equation integrators.

Link: [Cantera on Google Code](https://code.google.com/p/cantera/)

Link: [Cantera Information on the CMR Wiki](http://charlesmartinreid.com/wiki/CanteraOutline)

## What is Pantera?

Pantera (yes, like the metal band) is a set of programmer tools 
for people using Cantera in Python.

Cantera is an extremely useful library. This Python module will 
make it even more useful, by providing some functionality commonly
used in engineering calculations, and by giving you ideas about how
you can extend Cantera for your own uses.



# Installing Pantera

Pantera has a couple of dependencies. Once these are installed,
you can do the usual setup.py thing to install Pantera.

## Dependencies

In order to use Pantera, you will, at the very least, need to install Cantera. 
There are other features of Pantera that require other libraries. Their dependencies
are optional.

Required:
* Cantera
* JSON

Optional:
* Matplotlib
* itertools

## Installing

You can install Pantera by using setup.py:

```
python setup.py install
```

then import pantera like any other library:

```python
import pantera as pt
```

# Let's Get Started

Cool. We'll start with a tour of the Pantera module.

You can import the pantera library into Python:

```python
import pantera 

pantera_test() # doesn't work yet
```

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

Cantera is very handy for everyday engineering calculations. This submodule
creates some objects and methods that assist in these kinds of calculations.

```python
from pantera import *

h = Heater()
```

