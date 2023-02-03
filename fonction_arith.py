def isArith(liste):
    if len(liste) < 2:
        return False
    else:
        lng = len(liste) #longueur de la liste
        diff = liste[1]-liste[0] #Raison hypothetique de la suite
        for i in range(lng-1):
            if liste[i+1] - liste[i] != diff: #Onverifie que l'ecart est egale a l'hypothetique raison
                return False
        return True #Si tous les ecarts sont verifies, on renvoie alors True
