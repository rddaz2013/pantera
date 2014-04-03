from pantera.gases import * 
from Cantera import *

def mix1():
    T = 873.15
    P = OneAtm
    X = "CO2:2.0, CO:1.0"
    sol = Solution('gri30.xml')
    sol.set(T=T,P=P,X=X)
    return sol

def mix2():
    T = 973.15
    P = 3*OneAtm
    X = "CH4:8.0, C2H6:1.0"
    sol = Solution('gri30.xml')
    sol.set(T=T,P=P,X=X)
    return sol

def mix3():
    T = 1073.15
    P = 5*OneAtm
    X = "N2:10.0, HE:1.0"
    sol = Solution('gri30.xml')
    sol.set(T=T,P=P,X=X)
    return sol

def get_gases_to_mix():
    g1=mix1()
    g2=mix2()
    g3=mix3()
    return [g1,g2,g3]

def test_mixing():
    """Testing getGasMixture function"""
    gs = get_gases_to_mix()
    result = getGasMixture(gs,[1.0,1.0,2.0], model_file='gri30.xml', gas_phase_name='gri30')

#def test_composition()
#test_gas2compositions()
#test_composition_dicts()
#test_composition_strings()
#test_composition_vectors()
#
#def test_gas2compositions():
#convert_gas_to_composition_vector
#convert_gas_to_composition_dict
#convert_gas_to_composition_string
#
#def test_composition_dicts():
#convert_arrays_to_dict
#
#def test_composition_strings():
#convert_composition_string_to_dict()
#convert_composition_dict_to_string()
#
#def test_composition_vectors():
#	convert_composition_vector_to_dict()
#	convert_composition_dict_to_vector()

