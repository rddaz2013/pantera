from PistonCylinders import *

class AutoignitionReactor(IsobaricPC):
    """
    An autoignition reactor is a constant-pressure
    reactor containing a flammable mixture.

    The reactor is advanced in time until the mixture
    ignites.
    
    The autoignition delay time is defined as 
    the time to reach maximum rate of 
    temperature change:

    [$ 
    t_{aidt} = t | (dT/dt) = (dT/dt)_{max}
    $]

    The autoignition reactor needs to wrap the solve() method
    so that the simulation ends when the autoignition time
    has been found.
    """
    def __init__(self,contents=None,params={},**kwargs):
        """
        Autoignition reactors are perfectly adiabatic,
        and constant pressure.
        """
        # Call parent constructor first
        IsobaricPC.__init__(self,contents=contents,params=params,env_gas=None)

        # And we're done! 
        # We don't need to set anything else.

    def autoignition_time(self):
        # wrap calls to solve
        # compute dT/dt and d2T/dt2 at each point in time
        # once d2T/dt2 becomes negative, dT/dt stops increasing, 
        # and we have our autoigition time
        pass


