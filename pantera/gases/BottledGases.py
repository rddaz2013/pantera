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
            self.sol = ct.Solution('SanDiego201402_complete.cti')
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


