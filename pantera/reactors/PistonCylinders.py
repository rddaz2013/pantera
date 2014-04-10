from PanteraReactorBases import *

class PistonCylinder(PanteraReactor):
    """
    Defines a generic piston-cylinder system.
    """
    def __init__(self,contents=None,environment=None,params={},**kwargs):
        """
        Piston cylinder systems consist of a reactor with:
        * a wall (the piston)
        * an environment
        """
        # We'll call the parent constructor first
        PanteraReactor.__init__(self,contents,params,**kwargs)

        # Create the environment
        # (if none specified, use air at same TP as reactor contents)
        if environment == None:
            environment = Air()
            environment.TPX = self.T,self.thermo.P,"N2:0.79,O2:0.21"
        self.env = ct.Reservoir(environment)

        # Install the piston
        self.w = ct.Wall(self, self.env) 



# For convenience:
PC = PistonCylinder



class IsobaricPC(PC):
    """
    Isobaric piston-cyinder 
    (weightless piston)
    """
    def __init__(self,*args,**kwargs):
        PC.__init__(self,*args,**kwargs)

        # expansion parameter dV/dt = KA(P_1 - P_2)
        self.w.expansion_rate_coeff = 1.0e6 
        self.w.area = 1.0

class IsochoricPC(PC):
    """
    Isochoric piston-cyinder 
    (very heavy piston)
    """
    def __init__(self,**kwargs):
        PC.__init__(self,**kwargs)

        # expansion parameter dV/dt = KA(P_1 - P_2)
        self.w.expansion_rate_coeff = 0.0 
        self.w.area = 1.0

