import cantera as ct
from .gases import *
from .reactors import *
from .configurations import *

# this makes cantera available directly through pt namespace
# (dubious...)
from cantera import *



#################################
# Add the mechanisms directory to Cantera's search path
# so we don't have to copy XML files everywhere
import pkg_resources 
ct.add_directory( pkg_resources.resource_filename('pantera','mechanisms') )


#################################
# Monkey patch Cantera 

from cantera_monkey_patches import *

