from PanteraReactorBases import *

class PistonCylinder(PanteraReactor):
    """
    Defines a generic piston-cylinder system.
    """
    def __init__(self,contents=None,env_gas=None,params={},**kwargs):
        """
        Piston cylinder systems consist of a reactor with:
        * a wall (the piston)
        * an environment
        """
        # We'll call the parent constructor first
        PanteraReactor.__init__(self,contents,params={},**kwargs)

        # Create the environment 
        if env_gas == None:
            env_gas = Air()
            env_gas.set(Temperature=self._contents.temperature(),Pressure=self._contents.pressure())
        self.env = Reservoir(env_gas)

        # Install the piston
        self.w = Wall(self, self.env) 



# For convenience:
PC = PistonCylinder



class IsobaricPC(PC):
    """
    Isobaric piston-cyinder 
    (weightless piston)
    """
    def __init__(self,**kwargs):
        PC.__init__(self,**kwargs)
        self.w.set(K = 1.0e9, A = 1.0)# expansion parameter dV/dt = KA(P_1 - P_2)

class IsochoricPC(PC):
    """
    Isochoric piston-cyinder 
    (very heavy piston)
    """
    def __init__(self,**kwargs):
        PC.__init__(self,**kwargs)
        self.w.set(K = 1.0e-9, A = 1.0)# expansion parameter dV/dt = KA(P_1 - P_2)

