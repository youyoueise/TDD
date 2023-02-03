from fonction_arith import *

def genArith(liste,n):
    if isArith(liste) == False:
        return False
    else:
        raison = liste[1] - liste[0]
        new_liste = [liste[-1] + raison*(i+1) for i in range(n)]
        return [True,new_liste]
