from pantera import *
import numpy as np
from numpy import allclose
from functions import *



def test_PistonCylinder_empty():
    """
    Testing initialization of PistonCylinder with no inputs
    """
    pc = PistonCylinder()



def test_PistonCylinder_specify_contents():
    """
    Testing initialization of PistonCylinder with user-specified contents
    """
    T = 798.15
    P = one_atm
    X = "CH4:1.5, O2:3.0"
    g = get_gas(T,P,X)

    pc = PistonCylinder(contents=g)

    assert np.allclose(pc.T,T)
    assert np.allclose(pc.P,P)



def test_PistonCylinder_specify_contents_environment():
    """
    Testing initialization of PistonCylinder with user-specified contents and environment
    """
    T = 798.15
    P = one_atm
    X = "CH4:1.5, O2:3.0"
    g = get_gas(T,P,X)

    Te = 798.15
    Pe = one_atm
    Xe = "N2:0.79, O2:0.21"
    e = get_gas(Te,Pe,Xe)

    # create reactor
    pc = PistonCylinder(contents=g,environment=e)

    print pc.T
    assert np.allclose(pc.T,T)
    assert np.allclose(pc.P,P)



def test_PistonCylinder_specify_contents_inputparams():
    """
    Testing initialization of PistonCylinder with user-specified contents and input param dict
    """
    T = 798.15
    P = one_atm
    X = "CH4:1.5, O2:3.0"
    g = get_gas(T,P,X)

    input_params = {'dummyvar1':10.0,'dummyvar2':100.0}

    # create reactor
    pc = PistonCylinder(contents=g,params=input_params)

    assert np.allclose(pc.T,T)
    assert np.allclose(pc.P,P)

    c = pc._contents
    assert c!=None

    assert pc.params['dummyvar1']==10.0
    assert pc.params['dummyvar2']==100.0



def test_IsobaricPC_empty():
    """
    Testing initialization of IsobaricPC with no inputs
    """
    pc = IsobaricPC()



def test_IsobaricPC_specify_contents():
    """
    Testing initialization of IsobaricPC with user-specified contents
    """
    T = 798.15
    P = one_atm
    X = "CH4:1.5, O2:3.0"
    g = get_gas(T,P,X)

    pc = PistonCylinder(contents=g)

    assert np.allclose(pc.T,T)
    assert np.allclose(pc.P,P)



def test_IsobaricPC_specify_contents_environment():
    """
    Testing initialization of IsobaricPC with user-specified contents and environment
    """
    T = 798.15
    P = one_atm
    X = "CH4:1.5, O2:3.0"
    g = get_gas(T,P,X)

    Te = 798.15
    Pe = one_atm
    Xe = "N2:0.79, O2:0.21"
    e = get_gas(Te,Pe,Xe)

    # create reactor
    pc = IsobaricPC(contents=g,environment=e)

    assert np.allclose(pc.T,T)
    assert np.allclose(pc.P,P)



def test_IsobaricPC_specify_contents_inputparams():
    """
    Testing initialization of IsobaricPC with user-specified contents and input param dict
    """
    T = 798.15
    P = one_atm
    X = "CH4:1.5, O2:3.0"
    g = get_gas(T,P,X)

    input_params = {'dummyvar1':10.0,'dummyvar2':100.0}

    # create reactor
    pc = IsobaricPC(contents=g,params=input_params)

    assert np.allclose(pc.T,T)
    assert np.allclose(pc.P,P)

    c = pc._contents
    assert c!=None

    assert pc.params['dummyvar1']==10.0
    assert pc.params['dummyvar2']==100.0



def test_IsochoricPC_empty():
    """
    Testing initialization of IsochoricPC with no inputs
    """
    pc = IsochoricPC()



def test_IsochoricPC_specify_contents():
    """
    Testing initialization of IsochoricPC with user-specified contents
    """
    T = 798.15
    P = one_atm
    X = "CH4:1.5, O2:3.0"
    g = get_gas(T,P,X)

    pc = IsochoricPC(contents=g)

    assert np.allclose(pc.T,T)
    assert np.allclose(pc.P,P)



def test_IsochoricPC_specify_contents_environment():
    """
    Testing initialization of IsochoricPC with user-specified contents and environment
    """
    T = 798.15
    P = one_atm
    X = "CH4:1.5, O2:3.0"
    g = get_gas(T,P,X)

    Te = 798.15
    Pe = one_atm
    Xe = "N2:0.79, O2:0.21"
    e = get_gas(Te,Pe,Xe)

    # create reactor
    pc = IsochoricPC(contents=g,environment=e)

    print pc.T
    assert np.allclose(pc.T,T)
    assert np.allclose(pc.P,P)



def test_IsochoricPC_specify_contents_inputparams():
    """
    Testing initialization of IsochoricPC with user-specified contents and input param dict
    """
    T = 798.15
    P = one_atm
    X = "CH4:1.5, O2:3.0"
    g = get_gas(T,P,X)

    input_params = {'dummyvar1':10.0,'dummyvar2':100.0}

    # create reactor
    pc = IsochoricPC(contents=g,params=input_params)

    assert np.allclose(pc.T,T)
    assert np.allclose(pc.P,P)

    c = pc._contents
    assert c!=None

    assert pc.params['dummyvar1']==10.0
    assert pc.params['dummyvar2']==100.0




