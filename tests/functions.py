import pantera as pt 

def get_gas(T,P,X):
    g = pt.Solution('gri30.xml')
    g.TPX = T, P, X
    return g
