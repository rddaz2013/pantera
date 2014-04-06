from pantera import *
import numpy as np

def test_PanteraReactor():
    # make sure no params works
    pr0 = PanteraReactor()

    # test initialization with gas
    T = 798.15
    P = one_atm
    g = GRI30()
    g.TPX = T, P, "CH4:1.5, O2:3.0"
    input_params = {'dummyvar1':10.0,'dummyvar2':100.0}
    pr = PanteraReactor(contents=g,params=input_params)

    # test that Canter reactor methods 
    # were inherited properly
    assert pr.T == T
    assert np.allclose(pr.thermo.P,P)

    assert pr.params['dummyvar1']==10.0
    assert pr.params['dummyvar2']==100.0



