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
            self.TPX = 298.15, ct.one_atm, "N2:0.79,O2:0.21"
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
            return self.sol
        except AttributeError:
            self.sol = ct.Solution('gri30.xml')
            return self.sol


