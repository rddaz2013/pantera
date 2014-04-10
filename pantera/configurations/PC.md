# Piston Cylinder (PC) Reactors

The governing equation for piston cylinder systems and their 
volume change as a function of thermodynamic state is:

```
\frac{dV}{dt} = K A ( P_{left} - P_{right} )
```
[More about piston cylinder systems](pantera/configurations/PC.md)

## Initialization

Because piston cylinders are a single-reactor system, 
their initialization and solution is a mix of 
reactor and reactor network information. 
Our goal is not to interfere with this natural combination,
but to make it easier.

## Cantera Method

In Cantera, we have the necessary but awkward 
two-step process of creating the reactor,
and then creating the reactor network, 
and then installing the wall, 
and then setting the wall parameters,

```python
import cantera as ct

g = get_gas() # imaginary function returning a Solution object with TPX set
ctreactor = ct.Reactor(g)
ctnet = ct.ReactorNet([ctreactor])
ctnet.solve(0.01)
```

is all made much easier in Pantera.

* First, you initialize it like a reactor.

* Then, it sets the piston/wall parameters for you, 
    and dissolves the difference between a reactor
    and a reactor network.

* Finally, solve it like a ReactorNetwork.

Like so:

```python
import pantera as pt

g = get_gas() # imaginary function returning a Solution object with TPX set
pc = pt.PistonCylinderConfig(contents=g)
pc.solve(0.01)
```



Initialize the piston cylinder configuration the same
way you would a reactor:

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



