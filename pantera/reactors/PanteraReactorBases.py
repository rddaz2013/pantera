import cantera as ct
from ..gases.BottledGases import *

class CanteraReactor(ct.Reactor):
    """
    Monkey patch the Cantera reactor class
    """
    def get_P(self):
        return self.thermo.P
    def set_P(self,newP):
        self.thermo.P = newP
    P = property(get_P,set_P)

    def get_X(self):
        return self.thermo.X
    def set_X(self,newX):
        self.thermo.X = newX
    X = property(get_X,set_X)

    def get_contents(self):
        return self.thermo
    def set_contents(self):
        raise Exception("Error: Cantera reactor: you can't set the contents of a reactor directly.")
    _contents = property(get_contents,set_contents)

class PanteraReactor(CanteraReactor):
    """
    This is a very barebones extension of the
    Cantera Reactor type.

    It takes a dictionary of parameters
    in the constructor, functionality that can 
    be used to build sophisticated reactors
    that parse high-level input file 
    parameter specifications.
    """

    def __init__(self,contents=None,params={},**kwargs):
        """
        Saves input parameters for later.
        Constructs a Reactor by calling parent Reactor constructor.

        * contents - a Cantera Phase object; 
          the usual first argument to a Cantera 
          Reactor constructor
        * params - a dictionary of parameters,
          whatever the programmer wishes.
          The usefulness of this will become 
          clear in later examples.
        """

        # First, save the parameters
        self.params = params

        # Next, process the input parameters to 
        # check for required parameters, set default 
        # parameter values, etc.
        self.problemSetup()

        # If the user doesn't specify contents,
        # we'll fill it with air
        if contents == None:
            contents = Air()

        # Now call the parent constructor
        ct.Reactor.__init__(self,contents,**kwargs)

    def problemSetup(self):
        """
        The problemSetup method is intended to process
        the input parameter dictionary, self.params.
        
        It checks that required input parameters are specified,
        and sets any unspecified parameters to default values.

        This is one of the first methods a Pantera Reactor will call.

        The base class does not do anything interesting, so it doesn't
        need to process any input parameters.
        """
        pass

    def make_rxnpath(self,element,file_name,**options):
        """
        Output a reaction pathway for the current state of the gas in the reactor.
        Call this method while the reactor is running or after it has already run.
        Parameters:
        * element - which element to trace (usually 'C')
        * file_name - filename of output graphviz dot file
        * options - options to pass to graphviz dot
        """
        file_name += ".dot"
        rxnpath = ct.ReactionPathDiagram(self._contents, str(element))
        rxnpath.write_dot(file_name)

