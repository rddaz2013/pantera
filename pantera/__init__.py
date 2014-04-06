import cantera as ct
from .gases import *
from .reactors import *

from cantera import *



#################################
# Add the mechanisms directory to Cantera's search path
# so we don't have to copy XML files everywhere
import pkg_resources 
ct.add_directory( pkg_resources.resource_filename('pantera','mechanisms') )


#################################
# Extend Solution class so you can
# ask for specific species mass/mole fractions

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

ct.Solution.mole_fraction = mole_fraction

ct.Solution.mass_fraction = mass_fraction

#################################
# Monkey patch cantera 

OneAtm = ct.one_atm

ct.Solution.nSpecies = ct.Solution.n_species

#ct.Reactor.P = ct.Reactor.thermo.P

