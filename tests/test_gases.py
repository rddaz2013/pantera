from pantera import * 

def mix1():
    T = 873.15
    P = OneAtm
    X = "CO2:2.0, CO:2.0"
    sol = Solution('gri30.xml')
    sol.TPX = T,P,X
    return sol

def mix2():
    T = 973.15
    P = 3*OneAtm
    X = "CH4:8.0, C2H6:1.0"
    sol = Solution('gri30.xml')
    sol.TPX = T,P,X
    return sol

def mix3():
    T = 1073.15
    P = 5*OneAtm
    X = "N2:10.0, AR:1.0"
    sol = Solution('gri30.xml')
    sol.TPX = T,P,X
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

def test_gas2vector():
    """
    Testing conversion of gas to vector representation of composition.
    """
    g = mix1()

    lead_vector = convert_gas_to_composition_vector(g)

    gold_vector = zeros(g.n_species)
    gold_vector[g.species_index('CO2')] = 2.0
    gold_vector[g.species_index('CO')]  = 2.0

    # normalize
    gold_vector = gold_vector/sum(gold_vector)

    assert allclose(gold_vector,lead_vector,1.0e-5)

def test_gas2string():
    """
    Testing conversion of gas to string representation of composition.
    """
    g = mix1()

    lead_string = convert_gas_to_composition_string(g)

    gold_string = "CO2:0.5000000000000000, CO:0.5000000000000000"

    assert lead_string==gold_string

def test_gas2dict():
    """
    Testing conversion of gas to dict representation of composition.
    """
    g = mix1()

    lead_dict = convert_gas_to_composition_dict(g)

    gold_dict = {'CO2': 2.0, 'CO': 2.0}
    # normalize
    gold_sum = sum(gold_dict[k] for k in gold_dict)
    for k in gold_dict:
        gold_dict[k] = gold_dict[k]/gold_sum

    assert lead_dict==gold_dict

def test_arrays2dict():
    """
    Testing conversion of species names/fractions arrays to dict representation of composition.
    """
    names = ['CH4','C2H6','H2']
    moleFractions = [0.2,0.4,0.4]
    lead_dict = convert_arrays_to_dict(names,moleFractions)

    gold_dict = dict(zip(names, moleFractions))
    assert lead_dict==gold_dict


def test_vector2dict():
    """
    Testing conversion of species vector to species dict.
    """
    g = mix2()

    starting_vector = zeros(g.n_species,)

    starting_vector[g.species_index('CH4')] = 8.0
    starting_vector[g.species_index('C2H6')] = 1.0
    starting_vector = starting_vector/sum(starting_vector)

    lead_dict = convert_composition_vector_to_dict(g,starting_vector)

    gold_dict = {'CH4': 8.0, 'C2H6': 1.0}
    # normalize
    gold_sum = sum(gold_dict[k] for k in gold_dict)
    for k in gold_dict:
        gold_dict[k] = gold_dict[k]/gold_sum

    assert lead_dict==gold_dict

def test_dict2vector():
    """
    Testing conversion of species dict to species vector.
    """
    g = mix2()

    starting_dict = {'CH4': 8.0, 'C2H6': 1.0}

    lead_vector = convert_composition_dict_to_vector(g,starting_dict)

    gold_vector = zeros(g.n_species)
    gold_vector[ g.species_index('CH4') ] = 8.0
    gold_vector[ g.species_index('C2H6') ] = 1.0
    gold_vector = gold_vector/sum(gold_vector)

    assert allclose(lead_vector,gold_vector,1.0e-5)
    

def test_string2dict():
    """
    Testing conversion of species string to species dict.
    """
    g = mix2()

    starting_string = "CO2:2.0, CO:2.0"

    lead_dict = convert_composition_string_to_dict(starting_string)

    gold_dict = {}
    gold_dict['CO2'] = 2.0
    gold_dict['CO']  = 2.0

    # normalize
    gold_sum = sum( [gold_dict[k] for k in gold_dict.keys()] )
    for k in gold_dict.keys():
        gold_dict[k] = gold_dict[k]/gold_sum

    print lead_dict
    print gold_dict

    assert lead_dict==gold_dict

def test_dict2string():
    """
    Testing conversion of species dict to species string.
    """
    g = mix2()

