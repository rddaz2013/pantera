# Pantera: A Toolbox for Cantera in Python

Pantera is a toolbox for using and extending Cantera 2.1 [(link to latest Cantera tarball on Sourceforge)](http://sourceforge.net/projects/cantera/files/latest/download) with Python: [http://charlesreid1.github.io/pantera](http://charlesreid1.github.io/pantera)

Pantera is beta software. Pantera is _not_ a finished product!

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

# What's in the Pantera Library?

## Pantera Core

The core of the Pantera library is the source code in the ```pantera``` directory.
This is divided into various sub-modules.

You can explore the various submodules of Pantera
[at the Pantera core source code README.md file](pantera/README.md)

## Tests

The Pantera library uses nose as the unit testing framework. 
The ```tests``` directory contains nose tests that cover various
parts of the Pantera library.



# Getting Started

You can import the pantera library into Python like this:

```python
import pantera as pt
```

Once that import statement is working,
you can explore the various submodules of Pantera
[at the Pantera core source code README.md file](pantera/README.md)

