import pantera as pt
import numpy as np
from numpy import allclose
from functions import *



def test_PistonCylinder_empty():
    """
    Testing initialization of PistonCylinder with no inputs
    """
    pc = pt.PistonCylinderConfig()



def test_PistonCylinder_specify_contents():
    """
    Testing initialization of piston cylinder configuration with user-specified contents
    """
    T = 998.15
    P = pt.one_atm
    X = "CH4:1.5, O2:3.0"
    g = get_gas(T,P,X)

    pc = pt.PistonCylinderConfig(contents=g)

    assert np.allclose(pc.T,T)
    assert np.allclose(pc.P,P)

def test_PistonCylinder_shorthand_specify_contents():
    """
    Testing shorthand initialization of piston cylinder configuration with Cantera-style contents specification
    """
    T = 998.15
    P = pt.one_atm
    X = "CH4:1.5, O2:3.0"
    g = get_gas(T,P,X)

    pc = pt.PistonCylinderConfig(g)

    assert np.allclose(pc.T,T)
    assert np.allclose(pc.P,P)

    pci = pt.PistonCylinderConfig(g,energy='off')
    
    assert np.allclose(pci.T,T)
    assert np.allclose(pci.P,P)

def test_PistonCylinder_specify_contents_environment():
    """
    Testing initialization of PistonCylinder with user-specified contents and environment
    """
    T = 998.15
    P = pt.one_atm
    X = "CH4:1.5, O2:3.0"
    g = get_gas(T,P,X)

    Te = 998.15
    Pe = pt.one_atm
    Xe = "N2:0.79, O2:0.21"
    e = get_gas(Te,Pe,Xe)

    # create reactor
    pc = pt.PistonCylinderConfig(contents=g,environment=e)

    assert np.allclose(pc.T,T)
    assert np.allclose(pc.P,P)



def test_PistonCylinder_specify_contents_inputparams():
    """
    Testing initialization of PistonCylinder with user-specified contents and input param dict
    """
    T = 998.15
    P = pt.one_atm
    X = "CH4:1.5, O2:3.0"
    g = get_gas(T,P,X)

    input_params = {'dummyvar1':10.0,'dummyvar2':100.0}

    # create reactor
    pc = pt.PistonCylinderConfig(contents=g,params=input_params)

    assert np.allclose(pc.T,T)
    assert np.allclose(pc.P,P)

    c = pc._contents
    assert c!=None

    assert pc.params['dummyvar1']==10.0
    assert pc.params['dummyvar2']==100.0


