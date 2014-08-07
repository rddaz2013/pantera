import cantera as ct
from CanteraGasUtils import *

"""
==========================
Bottled Gases

Charles Reid
August 2013

==========================

This is a library of gases with various 
mechanisms and compositions.
Inspired by Cantera's GRI30().
"""

DEFAULT_MECH = 'gri30.xml'
DEFAULT_GAS_ID = 'gri30'

class Air(object):
    """
    Defines an air gas
    using the GRI 3.0 mchanism.
    """
    def __new__(self):
        try:
            return self.sol
        except AttributeError:
            self.sol = ct.Solution('gri30.xml')
            self.sol.TPX = 298.15, ct.one_atm, "N2:0.79,O2:0.21"
            return self.sol

class GRI30(object):
    """
    Defines a gas using the 
    GRI 3.0 mechanism.
    """
    def __new__(self):
        try:
            return self.sol
        except AttributeError:
            self.sol = ct.Solution('gri30.xml')
            return self.sol

class SanDiego(object):
    """
    Defines a gas using the 
    UC San Diego combustion mechanism
    web.eng.ucsd.edu/mae/groups/combustion/mechanism.html
    """
    def __new__(self):
        try:
            return self.sol
        except AttributeError:
            self.sol = ct.Solution('SanDiego.cti')
            return self.sol

class MethaneAir(object):
    """
    Defines a mixtue of methane and air
    in a proportion specified with 
    equivalence ratio phi. 
    """
    def __new__(self,phi=1.0):
        try:
            # if phi has changed, let's make a new gas
            if phi <> self.phi:
                raise PanteraGasChangedException
            return self.sol
        except AttributeError, PanteraGasChangedException:
            self.sol = ct.Solution('gri30.xml')
            meth_air_stoich = 1.0/2.0
            nox = 1
            nmeth = phi * meth_air_stoich
            nn2 = (0.79/0.21)*nox
            composition = "CH4:%0.5d,O2:%0.5d,N2:%0.5d"%(nmeth,nox,nn2)
            self.sol.TPX = 298.15, ct.one_atm, composition
            return self.sol

