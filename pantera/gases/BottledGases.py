from Cantera import *
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
            		self.sol = GRI30()
            		return self.sol


