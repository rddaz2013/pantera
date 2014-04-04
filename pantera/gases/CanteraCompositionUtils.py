import cantera as ct
import itertools 
from numpy import *

"""
=============================
Cantera Composition Utility Functions 

Charles Reid
August 2013

=============================
There are three methods for specifying
gas compositions:
* String, e.g. "CH4:1.0, O2:1.0"
* Vector, e.g. [0.0, 0.1, 0.75, 1.5, 2.2, 1.0e-5]
* Dict, e.g. d['CH4'] = 1.0; d['O2'] = 1.0

(Note that the dict method is not supported by
Cantera, it is simply a more convenient way
of dealing with compositions.)

We want to be able to do a couple of things:
1. Turn gases into strings/vectors/dicts
2. Turn vectors into dicts and dicts into vectors
3. Turn strings into dicts and dicts into strings



Functions defined in file:

Converting gases to composition vectors, dicts, and strings:
+ convert_gas_to_composition_vector
+ convert_gas_to_composition_dict
+ convert_gas_to_composition_string
+ convert_arrays_to_dict

Converting between composition vectors and dicts:
+ convert_composition_vector_to_dict
+ convert_composition_dict_to_vector

Converting between composition strings and dicts:
+ convert_composition_string_to_dict
+ convert_composition_dict_to_string

Gas mixing:
+ getGasMixture( gases, Xs )
"""


# ==========================================
# Turning gases into a composition representation:
# ==========================================

def convert_gas_to_composition_vector( gas ):
    """
    Converts a Cantera gas with a specified composition into
    a composition vector of mole fractions
    """
    return gas.X

def convert_gas_to_composition_dict( gas ):
    """
    Converts a Cantera gas with a specified composition into
    a composition dict of mole fractions
    """
    d = {}
    for sp in gas.species_names:
        if gas.mole_fraction(sp) > 0.0:
            d[sp] = gas.mole_fraction(sp)
    return d

def convert_gas_to_composition_string( gas ):
    """
    Converts a Cantera gas with a specified composition into
    a representative composition string of style "CH4:1.0, N2:4.0"
    """
    d = convert_gas_to_composition_dict(gas)
    s = convert_composition_dict_to_string(d)
    return s


def convert_arrays_to_dict(speciesNames,moleFractions):
    """
    Converts two vectors, one containing species names and 
    one containing mole fractions, into a species dictionary
    """
    d = {}
    assert len(speciesNames) == len(moleFractions)
    for name, amt in zip(speciesNames,moleFractions):
        d[name] = amt
    return d


# ==========================================
# Converting between composition vectors and dicts:
# ==========================================

def convert_composition_vector_to_dict( g, Xv ):
    """Convert a composition vector Xv into a dict, for a given gas g"""
    Xd = {}
    for iv, v in enumerate(Xv):
        if v > 0.0:
            Xd[g.species_name(iv)] = v
    return Xd

def convert_composition_dict_to_vector( g, Xd ):
    """Convert a composition dict Xd into a vector, for a given gas g"""
    Xv = zeros( g.n_species, )
    for k in Xd.keys():
        Xv[g.species_index(k)] = Xd[k]
    Xv = Xv/sum(Xv)
    return Xv


# ==========================================
# Converting between composition strings and dicts:
# ==========================================

def convert_composition_string_to_dict( X ):
    """
    Converts a composition string of style "CH4:0.02, N2:0.01, O2:0.45"
    into a dict, a la composition['CH4'] = 0.02
    """
    results = {}
    for sp in X.split(","):
        st = sp.strip()
        try:
            results[ st.split(":")[0].strip() ] = float( st.split(":")[1].strip() )
        except IndexError:
            # X is probably not a list
            # (why would we run split on a list?)
            # or is empty
            err = "ERROR: CanteraGasUtils: your X is probably specified incorrectly. Expected type list, got type "+type(X)
            raise Exception(err)

    # normalize
    results_sum = sum( [results[k] for k in results.keys()] )
    for k in results.keys():
        results[k] = results[k]/results_sum

    return results

def convert_composition_dict_to_string( d ):
    """
    Converts a composition dict of stype composition['CH4'] = 0.02,
    into a string like "CH4: 0.02"
    """
    X = ""
    for item in d:
        if d[item] > 0.0:
            X += "%s:%0.16f"%(item,d[item])
            X += ", "
    X=X[:-2]
    return X


