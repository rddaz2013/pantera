from pantera import *

def test_SanDiego():
    """
    Testing solutions that use the San Diego mechanism
    """
    sd = SanDiego()

    # verify something about 
    # san diego
    # (nspecies? something?)

def test_MethaneAir():
    """
    Testing methane-air solutions 
    """
    ma1 = MethaneAir()

    # verify mole fractions match
    # using numpy compare arrays

    phi = 1.0
    ma2 = MethaneAir(phi=phi)

    phi = 3.0
    ma3 = MethaneAir(phi=phi)

