from pantera import *
import numpy as np

def get_gas(T,P,X):
    g = GRI30()
    g.TPX = T, P, X
    return g

def test_PanteraReactor1():
    """
    Testing barebones initialization of PanteraReactor
    """

    # make sure no params works
    pr = PanteraReactor()

def test_PanteraReactor2():
    """
    Testing initialization of PanteraReactor with user-specified contents/input parameters
    """

    # prep contents/input params
    T = 798.15
    P = one_atm
    X = "CH4:1.5, O2:3.0"
    g = get_gas(T,P,X)
    input_params = {'dummyvar1':10.0,'dummyvar2':100.0}

    # create reactor
    pr = PanteraReactor(contents=g,params=input_params)

    # test that Canter reactor methods 
    # are extended/inherited properly 
    assert np.allclose(pr.T,T)
    assert np.allclose(pr.P,P)

    # test that we can access reactor properties
    # defined by Pantera library
    c = pr._contents
    assert c != None

    # test that we can access our input parameter values
    assert pr.params['dummyvar1']==10.0
    assert pr.params['dummyvar2']==100.0


def test_PistonCylinder1():
    """
    Testing barebones initialization of piston-cylilnder
    """
    pc = PistonCylinder()

def test_PistonCylinder2():
    """
    Testing initialization of piston-cylinder with user-specified contents/input parameters
    """
    # test initialization with gas
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

    assert pr.params['dummyvar1']==10.0
    assert pr.params['dummyvar2']==100.0

def test_PistonCylinder3():
    """
    Testing initialization of piston-cylinder with weightless piston 
    """
    pass



