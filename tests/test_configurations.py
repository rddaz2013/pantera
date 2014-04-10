import pantera as pt
import cantera as ct
import numpy as np
from numpy import allclose
from functions import *

def get_gas():
    g = pt.Solution('SanDiego.cti')
    g.TPX = 898.15, 9*ct.one_atm, "C2H6:1.0, O2:4.0"
    return g

def test_cantera_reactornet():
    """
    Testing basic Cantera ReactorNet functionality
    """
    g = get_gas()
    ctreactor = ct.Reactor(g)
    ctnet = ct.ReactorNet([ctreactor])
    ctnet.advance(0.01)

def test_configuration():
    """
    Testing basic Pantera Configuration functionality
    """
    g = get_gas()
    ptreactor = pt.PanteraReactor(g)
    ptconfig = pt.Configuration([ptreactor])
    ptconfig.advance(0.01)

def test_piston_cylinder_config():
    """
    Testing basic piston cylinder configuration functionality
    """
    g = get_gas()
    pc = pt.PistonCylinderConfig(g)
    pc.advance(0.01)



