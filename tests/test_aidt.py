import pantera as pt
import numpy as np
from numpy import allclose
from functions import *



def get_autoignition_input_dict():
    d = {}
    return d



def test_AutoignitionReactor_specify_contents():
    """
    Testing initialization of autoignition reactor with user-specified gas contents
    """
    g = GRI30()
    T = 798.15
    P = one_atm
    X = "CH4:1.5, O2:3.0, H:0.00001"
    g.TPX = T,P,X

    a = AutoignitionReactor(contents=g)



def test_AutoignitionReactor_specify_contents_inputparams():
    pass
    T = 798.15
    P = one_atm
    X = "CH4:1.5, O2:3.0"
    g = get_gas(T,P,X)

    input_params = get_autoignition_dict()

    a = AutoignitionReactor(contents=g,params=input_params)

