import Cantera
import itertools 
from numpy import *

"""
=============================
Cantera Gas Utility Functions

Charles Reid
August 2013

=============================
It is often convenient to be able to
take multiple gas objects of various 
compositions and mix them all together
in specified proportions.

This function allows for specifying 
mass, mole, or volume fractions.

Note that each gas must have a common
XML file, so that the final mixture
shares species.
"""


# =======================================
# Gas mixing:
# =======================================

def getGasMixture( gases,     # list of gases
                   Xs,        # list of moles/mole fractions of each gas
                   Ws = None, # list of weights/weight fractions of each gas[sensible/my notation]
                   Ys = None, # list of masses/mass fractions of each gas[Cantera notation]
                   Vs = None, # list of volumes/vol fractions of each gas
                   model_file=None, 
                   gas_phase_name=None ):
    """
    Convert a list of gases and mole fractions
    (or mass fractions, or volume fractions, 
    or partial pressures, eventually)
    into a single Gas mixture.
    Do this by manually computing 
    mass-averaged mixture enthalpy,
    mole-averaged pressure,
    and composition mixing via composition dict
    """

    if model_file == None or gas_phase_name == None:
        err = "ERROR: CanteraGasUtils: You must specify a model file (via params['model_file']) and gas phase name (via params['gas_phase_name']) for the gas mixture."
        raise Exception(err)

    # pass in a normalized Xs
    Xsarr = array(Xs)
    Xsnorm = Xsarr/sum(Xsarr) 

    # technically a little better, 
    # but setting HPX is expensive 
    # (Newton iterations over T)
    #try:
    #    H, P, X = mixture_HPX( gases, Xnorm )
    #except CanteraError:
    #    T, P, X = mixture_TPX( gases, Xsnorm )

    # this approximates constant Cp
    # (i.e, only works for limited T differences 
    #       among geses being mixed):
    T, P, X = mixture_TPX( gases, Xsnorm )
    gas = Cantera.importPhase(model_file,gas_phase_name)
    gas.set(T=T,P=P,X=X)

    return gas


def mixture_TPX( gases, Xs, verbosity=0):
    """
    Given a list of gases and their mole fractions,
    this returns the TPX info needed to create
    a Cantera Gas object that is 
    a mixture of these gases.
    """

    # --------------
    # X

    mixture_d = {}

    if verbosity > 0:
        print "Looping over all species of all gases to make a new mixture:"
    for gas,wx_i in zip(gases,Xs):
        for sp in gas.speciesNames():
            if verbosity > 0:
                if sp == 'CH3':
                    print "CH3 mole frac = %0.4g"%(gas.moleFraction(sp))
            if sp in mixture_d:
                mixture_d[sp] += wx_i * gas.moleFraction(sp)
            elif gas.moleFraction(sp) != 0.0: 
                mixture_d[sp] = wx_i * gas.moleFraction(sp)
            else:
                pass

    mixture_s = convert_composition_dict_to_string(mixture_d)
    if verbosity > 0:
        print "Mixing resulted in gas with X = "+mixture_s

    # --------------
    # H

    # Compute Tmix with molar heat capacities
    #
    # Define:
    # h_mix = C_pmix T_mix = ( sum_i n_i C_pi Ti )/( n_T )
    #
    # from which we get relationship:
    # T_mix = \sum_i [ (x_i C_pi )/( C_pmix ) ] T_i

    # first compute c_pmix
    cp_mix = 0
    for gas, wx_i in zip(gases,Xs):
        cp_mix += wx_i * gas.cp_mole()

    # next compute T_mix
    T_mix = 0
    for gas, wx_i in zip(gases,Xs):
        coeff = ( wx_i * gas.cp_mole() )/( cp_mix )
        T_mix += coeff * gas.temperature()

    # --------------
    # P

    press = 0.0
    for gas,wx_i in zip(gases,Xs):
        press += wx_i * gas.pressure() 

    # -------------------
    # Return TPX
    
    return T_mix, press, mixture_s


def mixture_HPX( gases, Xs ):
    """
    Given a mixture of gases and their mole fractions,
    this method returns the enthalpy, pressure, and 
    composition string needed to initialize 
    the mixture gas in Cantera.

    NOTE: The method of setting enthalpy 
    usually fails, b/c Cantera uses a Newton
    iterator to find the temperature that
    yields the specified enthalpy, and it 
    isn't very robust.
    Instead, approximate constant Cp's
    and find T_mix manually, as with the
    mixture_TPX() method above.
    """

    # --------------
    # X

    mixture_d = {}

    for gas,wx_i in zip(gases,Xs):
        for sp in gas.speciesNames():
            if sp in mixture_d:
                mixture_d[sp] += wx_i * gas.moleFraction(sp)
            elif gas.moleFraction(sp) != 0.0: 
                mixture_d[sp] = wx_i * gas.moleFraction(sp)
            else:
                pass

    mixture_s = convert_composition_dict_to_string(mixture_d)

    # --------------
    # H

    # Compute Tmix with molar heat capacities
    #
    # Define:
    # h_mix = sum_i n_i h_i 
    #
    # where h is molar enthalpy

    # compute H_mix
    H_mix = 0
    for gas, wx_i in zip(gases,Xs):
        Hmix += wx_i * gas.enthalpy_mole()

    # --------------
    # P

    press = 0.0
    for gas,wx_i in zip(gases,Xs):
        press += wx_i * gas.pressure() 

    # -------------------
    # Return HPX
    
    return H_mix, press, mixture_s

