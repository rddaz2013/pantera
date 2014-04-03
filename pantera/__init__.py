from cantera import Solution
from .gases import *
from .reactors import *

# bring back the old stuff
OneAtm = one_atm

# monkey patch solutions to make
# mole fraction queries easier
def mole_fraction(self,speciesName):
    return self[speciesName].X

def mass_fraction(self,speciesName):
    return self[speciesName].Y

Solution.mole_fraction = mole_fraction
Solution.mass_fraction = mass_fraction
