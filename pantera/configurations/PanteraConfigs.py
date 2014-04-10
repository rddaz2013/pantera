import cantera as ct
from ..reactors.PanteraReactorBases import *

class Configuration(ct.ReactorNet):
    """
    Default behavior: reactor network wraps a single reactor
    Initialize it like a reactor,
    advance()/solve() it like a reactor network.

    If you have a different scenario, your constructor and solve
    will look different.
    """

    def __init__(self,contents=None,params={},**kwargs):
        """
        Initialize the piston cylinder system
        """
        # first call reactor constructor
        self.r = PanteraReactor(contents=contents,params=params,**kwargs)

        # now call reactor network constructor
        ct.ReactorNet.__init__(self,[self.r])

        # now, we're done! 
        # it will behave exactly like a normal reactornet now
        # hence, the constructor of a reactor,
        # and the functionality of a reactor network

    # Oh yeah - we may want to define some of the same 
    # properties that reactors have.

    # P pressure property
    def get_P(self):
        return self.r.P
    def set_P(self,newP):
        self.r.P = newP
    P = property(get_P,set_P)

    # T pressure property
    def get_T(self):
        return self.r.T
    def set_T(self,newT):
        self.r.T = newT
    T = property(get_T,set_T)

    # Y mass frac property
    def get_Y(self):
        return self.r.Y
    def set_Y(self,newY):
        self.r.Y = newY
    Y = property(get_Y,set_Y)

    # X mole frac property
    def get_X(self):
        return self.r.X
    def set_X(self,newX):
        self.r.X = newX
    X = property(get_X,set_X)

    # params property
    def get_params(self):
        return self.r.params
    def set_params(self):
        raise Exception("Error: can't set input parameter dictionary")
    params = property(get_params,set_params)

    # _contents property
    def get_contents(self):
        return self.r._contents
    def set_contents(self,content):
        self.r.insert(contents)
    _contents = property(get_contents,set_contents)


