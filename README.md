pantera
=======

A toolbox for using and extending Cantera in Python.

## What is Cantera?

Cantera is an object-oriented toolkit for chemical kinetics! 

Link: [Cantera on Google Code](https://code.google.com/p/cantera/)

Link: [Cantera Information on the CMR Wiki](http://charlesmartinreid.com/wiki/CanteraOutline)

## What is Pantera?

Pantera (yes, like the metal band) is a set of programmer tools 
for people using Cantera in Python.

## A Quick Tour

Import the pantera library into Python:

```python
import pantera 
```

### Gases

Pantera defines several utility functions
for things like specification of composition,
conversion of formats, mixing of gases, and 
others.

```python
from pantera.gases import *
```

### Reactors 

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







