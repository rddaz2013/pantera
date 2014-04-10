"""
plug flow reactors
length-based

constant flowrate
continuity equation

series of N cstrs
each cstr has a volume equal to total volume / N reactors

solve:
    for each reactor:
        create inlet, outlet, cstr
        equilibrate reactor
        create reservoir with results contents for inlet

cstr train
"""

class PlugFlowReactor(PanteraReactor):
    def __init__(self,*args,**kwargs):
        PanteraReactor.__init__(self,*args,**kwargs)

        # make N reactors

