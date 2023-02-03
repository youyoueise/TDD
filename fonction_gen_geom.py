from fonction_geom import *

def genGeom(liste,n):
    if isGeom(liste) == False:
        return False
    else:
        raison = liste[1]/liste[0]
        new_liste = [liste[-1]*(raison**(i+1)) for i in range(n)]
        return [True,new_liste]
