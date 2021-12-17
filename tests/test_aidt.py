import pantera as pt
import numpy as np
from numpy import allclose
from functions import *



def get_autoignition_dict():
    return {}



def test_AutoignitionReactor_specify_contents():
    """
    Testing initialization of autoignition reactor config with user-specified gas contents
    """
    g = pt.GRI30()
    T = 998.15
    P = pt.one_atm
    X = "CH4:1.5, O2:3.0, H:0.00001"
    g.TPX = T,P,X

    a = pt.AutoignitionConfig(contents=g)



def test_AutoignitionReactor_specify_contents_inputparams():
    """
    Testing initialization of autoignition reactor config with user-specified gas contents and input params
    """
    g = pt.GRI30()
    T = 998.15
    P = pt.one_atm
    X = "CH4:1.5, O2:3.0"
    g.TPX = T,P,X

    input_params = get_autoignition_dict()

    a = pt.AutoignitionConfig(contents=g,params=input_params)

