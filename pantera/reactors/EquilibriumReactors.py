from PanteraReactorBases import *

"""
overload solve method
to run equilibrate() on contents
"""

class EquilibriumReactor(PanteraReactor):
    def solve(self):
        self._contents.equilibrate('TP') 

