def isGeom(liste):
    if len(liste) < 2 or liste[0] == 0:
        return False
    else:
        raison = liste[1]/liste[0] #Raison hypothetique de la suite
        lng = len(liste) #longueur de la liste
        for i in range(lng-1):
            if liste[i] == 0: #On verifie qu'on a pas de divisions par 0
                return False
            else:
                if liste[i+1]/liste[i] != raison: #On verifie que l'ecart est egale a l'hypothetique raison
                    return False
        return True #Si tous les ecarts sont verifies, on renvoie alors True
