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

You can install Pantera by using setup.py:

```
python setup.py install
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

fuel = MethaneAir()
```

[Visit the gases README.md for details](pantera/gases/README.md)

## Reactors submodule

You can create Pantera reactor objects. These 
extend Cantera's Reactor classes.

You can import all of Pantera, keeping your namespace clean:

```python
import pantera

pr = pantera.PanteraReactor()
```

or just import some of Pantera, directly into the namespace:

```python
from pantera.reactors import *

pr = PanteraReactor()
```

[Visit the reactors README.md for details](pantera/reactors/README.md)


