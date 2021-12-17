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

        parameters:
        * contents - reactor contents initialized with this Cantera Solution
        * params - input parameter dictionary
        """
        # Call parent constructor first
        IsobaricPC.__init__(self,contents=contents,params=params,env_gas=None)

        self.problem_setup()

        if contents is None:
            g = GRI30()

            # how to see if X in 
            if 'X' in self.__dict__:
                g.TPX = self.T, self.P, self.X

            elif 'Y' in self.__dict__:
                g.TPY = self.T, self.P, self.Y

            self.insert(g)

    def problem_setup(self):
        """
        The input parameters may specify
        TPX/TPY
        If you wanna do anything more fancy,
        make a Solution yourself, and pass it
        as the reactor contents.
        """
        self.problem_setup_composition()
        self.problem_setup_pressure()
        self.problem_setup_temperature()

    def problem_setup_composition(self):
        """
        Check for X or Y specified
        """
        if 'X' in self.params:
            self.X = self.params['X']
        elif 'Y' in self.params:
            self.Y = self.params['Y']

    def problem_setup_pressure(self):
        pass

    def problem_setup_temperature(self):
        pass

    def autoignition_time(self):
        # wrap calls to solve
        # compute dT/dt and d2T/dt2 at each point in time
        # once d2T/dt2 becomes negative, dT/dt stops increasing, 
        # and we have our autoigition time
        pass


