# Gases

This directory contains objects and functions that
make dealing with gases and gas compositions easier.

## Bottled Gases

This is a virtual cabinet of various mixtures.
These create a shorthand way of doing things,
like creating a methane-air mixture and specifying
its equivalence ratio:

```python
from pantera.gases import *

ready_to_ignite = MethaneAir(phi=0.5)
```

## Cantera Composition Utilities

Cantera provides the user with two ways of specifying 
composition, neither of which are particularly
convenient for programming purposes:

1. Specify composition by string, e.g., "CH4:1.0, O2:8.0"

2. Specify composition by vector, e.g., [0.0, 0.7, 9.0, 15.3, 0.0, 1.0e-5]

The first way is cumbersome for converting back and forth between 
molar or volume ratios, and the second way is cumbersome for the
user to specify by hand (which vector index corresponds to which 
species index is dictated by their order in the XML file, and is 
usually random).

To resolve this, I've added a third method for specifying 
composition that resolves that, and it is the compsition dict:

```python
d={}
d['CH4'] = 1.0
d['O2']  = 8.0*d['CH4']
d['N2']  = (0.79/0.21)*d['O2']
```

Now we have our mixture.

Composition dicts allow you to specify, with strings, things that
are natural to express with strings, and to specify things with formulas
that are natural to specify with formulas. 

This file provids functions for converting between each of these types,
as well as converting back and forth between these composition 
specification methods and Cantera gas phase objects.

### Converting Gases to Composition Formats

Converting gases to composition vectors, dicts, and strings:

```
convert_gas_to_composition_vector
convert_gas_to_composition_dict
convert_gas_to_composition_string
```

### Composition Dict Specification

```
convert_arrays_to_dict
```

### Composition Vector Specification

Converting between composition vectors and dicts:

```
convert_composition_vector_to_dict
convert_composition_dict_to_vector
```

### Composition String Specification

Converting between composition strings and dicts:

```
convert_composition_string_to_dict
convert_composition_dict_to_string
```

## Cantera Gas Utilities

This implements the ability to create a set of
Cantera phase objects, each with various 
thermochemical states, and mix them all 
together. It then returns the mixture
as a single Cantera gas object.

You can specify your mixing proportions
by mole, mass, or volume fraction.

```python
from pantera import *
from copy import deepcopy

gs = [Solution('gri30.xml'),
      Solution('gri30.xml'),
      Solution('gri30.xml')]

Ts = [873.15, 973.15, 1073.15]
Ps = [OneAtm, 2*OneAtm, 3*OneAtm]
Xs = ["CO2:1.0", "N2:0.79, O2:0.21", "C2H6:1.0, CH4:10.0"]

for g,T,P,X in zip(gs,Ts,Ps,Xs):
	set(g,T=T,P=P,X=X)

getGasMixture(gs,[1.0,1.0,2.0],model_file='gri30.xml',gas_phase_name='gri30')
```

Beware!!! the otherwise-pythonic

```python
gs = [Solution('gri30.xml'),]*3
```

does not work, because it initializes a list with 3 versions of the 
same underlying object. When you modify one of them, you modify all of them.

Ooops!

Ideally, you would be able to grab the XML file
and gas phase name from each gas object, and ensure
they all match. But I haven't looked into this yet.

