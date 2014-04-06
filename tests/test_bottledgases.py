fom pantera import *

def test_SanDiego():
    sd = SanDiego()

    # verify something about 
    # san diego
    # (nspecies? something?)

def test_MethaneAir():
    ma1 = MethaneAir()

    # verify mole fractions match
    # using numpy compare arrays

    phi = 1.0
    ma2 = MethaneAir(phi=phi)

    phi = 3.0
    ma3 = MethaneAir(phi=phi)

