# Pantera Reactors

Specification of logic behind design

inheritance

self.params

problemSetup

## Pantera Reactor Bases

Contains base classes that define common functionality
for all Pantera reactors (specifically, taking a dictionary
of reactor input parameters, and defining a problem setup
method that processes these input parameters.

## Piston Cylinder (PC) Reactors

You can either create your own piston-cylinder system,
which can take whatever input parameters you want to define,
or you can use some of the provided piston-cylinder classes below.

Piston cylinder systems are defined as a reactor 
that contains a flexible wall between itself and
an environment. The expansion of the reactor 
is proportional to the pressure drop across the wall:

```latex
\frac{dV}{dt} = K A ( P_{left} - P_{right} )
```

### Isobaric PC (Weightless Piston)

An isobaric piston-cylinder has a constant pressure, 
which requires the proportionality constant K to be
very large, e.g.:

```
K = 1.0e6
```

#### Adiabatic 

To make an adiabatic isobaric piston-cylinder system,
remember that we are inheriting Cantera Reactor types,
so we can pass any parameters that Cantera Reactors take.

To make an adiabatic isobaric piston cylinder, we pass
the ```energy='on'``` option:

```python
import pantera as pt

g = pt.Solution('gri30.xml')
g.TPX = 898.15, pt.one_atm, "C2H6:1.0, O2:4.0"

e = pt.Solution('gri30.xml')
e.TPX = 898.15, pt.one_atm, "N2:0.79, O2:0.2"

pc = pt.IsobaricPC(contents=g,energy='on')
```

#### Isothermal

Same as above, except now we pass ```energy='off'```:

```python
import pantera as pt

g = pt.Solution('gri30.xml')
g.TPX = 898.15, pt.one_atm, "C2H6:1.0, O2:4.0"

e = pt.Solution('gri30.xml')
e.TPX = 898.15, pt.one_atm, "N2:0.79, O2:0.2"

pc = pt.IsobaricPC(contents=g,energy='off')
```

### Isochoric PC (Heavy Piston)

Isochoric piston-cylinders have a constant volume, so
the expansion coefficient is zero to prevent any
expansion: 

```python
K = 0
```

### Adiabatic

Pass ```energy='on'``` to constructor

### Isothermal

Pass ```energy='off'``` to constructor

