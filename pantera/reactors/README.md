# Pantera Reactors

Specification of logic behind design

inheritance

self.params

problemSetup

## 

## Piston Cylinder (PC) Reactors

You can either create a piston-cylinder system yourself, and specify
all of the parameters for the piston yourself,
or you can use some of the classes below for more brevity.

### Isobaric PC (Weightless Piston)

Sets K = 0

#### Adiabatic 

remember that we are inheriting Cantera Reactor types

so energy equation behavior is same as Cantera reactors (adiabatic by default)

we make these reactors adiabatic/isothermal the same way we make Cantera reactors adiabatic/isothermal

pass in energy='on'

example

#### Isothermal

pass in energy='off'

example

### Isochoric PC (Heavy Piston)

Sets K = Big

### Adiabatic

pass in energy='on'

example

### Isothermal

pass in energy='off'

example

