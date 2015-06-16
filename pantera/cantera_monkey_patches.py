import cantera as ct
#from cantera import *

#################################
# Monkey patch Cantera constants

# bars
one_bar = ct.one_atm*(1.0e5/1.01325e5)
OneBar = one_bar

# atms
OneAtm = ct.one_atm

#################################
# Monkey patch Cantera Solution class

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

ct.Solution.nSpecies = ct.Solution.n_species
ct.Solution.nReactions = ct.Solution.n_reactions

################################
# Monkey patch Cantera Reactor class

def get_contents(self):
    return self.thermo

#ct.Reactor._contents = get_contents
#ct.Reactor.P = ct.Reactor.thermo.P
#ct.Reactor.X = ct.Reactor.thermo.X
#ct.Reactor.mole_fractions = ct.Reactor.X

