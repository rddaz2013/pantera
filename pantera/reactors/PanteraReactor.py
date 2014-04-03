from Cantera import *
from Cantera.Reactor import *

class PanteraReactor(Reactor):
    """
    This is a very barebones extension of the
    Cantera Reactor type.

    It takes a dictionary of parameters
    in the constructor, functionality that can 
    be used to build sophisticated reactors
    that parse high-level input file 
    parameter specifications.
    """

    def __init__(self,contents=None,params={}):
        """
        Constructs a Pantera reactor.
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

        # If the user doesn't specify contents,
        # we'll fill it with air
        if contents == None:
            contents = Air()

        # Now call the parent constructor
        Reactor.__init__(self,contents)

