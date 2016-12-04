import pantera as pt
import numpy as np
from numpy import allclose
from functions import *



def test_PanteraReactor_empty():
    """
    Testing initialization of PanteraReactor 
    with no inputs
    """

    # make sure no params works
    pr = pt.PanteraReactor()



def test_PanteraReactor_contents_inputparams():
    """
    Testing initialization of PanteraReactor 
    with user-specified contents and input param dict
    """

    # prep contents/input params
    T = 998.15
    P = pt.one_atm
    X = "CH4:1.5, O2:3.0"
    g = get_gas(T,P,X)
    input_params = {'dummyvar1':10.0,'dummyvar2':100.0}

    # create reactor
    pr = pt.PanteraReactor(contents=g,params=input_params)

    # test that Canter reactor methods 
    # are extended/inherited properly 
    assert np.allclose(pr.T,T)
    assert np.allclose(pr.P,P)

    # test that we can access reactor contents,
    # a property defined by the Pantera library
    c = pr._contents
    assert c != None

    # test that we can access our input parameter values
    assert pr.params['dummyvar1']==10.0
    assert pr.params['dummyvar2']==100.0













