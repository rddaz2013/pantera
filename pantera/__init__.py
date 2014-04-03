from cantera import Solution
from .gases import *
from .reactors import *

# Monkey patch cantera so that the old ways of using it still work

OneAtm = one_atm

def mole_fraction(self,speciesName):
    X = self[speciesName].X

    if len(X) > 1:
        return X
    else:
        return X[0]

def mass_fraction(self,speciesName):
    Y = self[speciesName].Y

    if len(Y) > 1:
        return Y
    else:
        return Y[0]

Solution.mole_fraction = mole_fraction

Solution.mass_fraction = mass_fraction

Solution.nSpecies = Solution.n_species



