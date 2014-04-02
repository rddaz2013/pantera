from pantera.gases import * 

def get_three_gases():
	gs = [GRI30()]*3
	Ts = [873.15, 973.15, 1073.15]
	Ps = [OneAtm, 2*OneAtm, 3*OneAtm]
	Xs = ["CO2:1.0", "N2:0.79, O2:0.21", "C2H6:1.0, CH4:10.0"]

	for gas,T,P,X in zip(gs,Ts,Ps,Xs):
		set(gas,T=T,P=P,X=X)
	return *gs

def test_mixing():
	g1, g2, g3 = get_three_gases()

def test_composition():
	test_gas2compositions()
	test_composition_dicts()
	test_composition_strings()
	test_composition_vectors()

def test_gas2compositions():
	convert_gas_to_composition_vector
	convert_gas_to_composition_dict
	convert_gas_to_composition_string

def test_composition_dicts():
	convert_arrays_to_dict

def test_composition_strings():
	convert_composition_string_to_dict()
	convert_composition_dict_to_string()

def test_composition_vectors():
	convert_composition_vector_to_dict()
	convert_composition_dict_to_vector()

