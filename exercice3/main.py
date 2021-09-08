def imposable():
    """Permet de determiner sur l'habitant est imposable"""
    resultat = ""
    sexe = input("Etes-vous un homme ou une femme,taper H ou F ")
    if(sexe == "H"):
        sexe = True
    elif(sexe == "F"):
        sexe = False
    else:
        resultat = "Erreur dans la valeur entrer fermeture du programme "
        return resultat
        
    age = int(input("Entrez votre age "))

    if(sexe and age > 20):
        resultat = "Vous etes imposable"
    elif(not sexe and age >= 18 and age <=35):
        resultat = "Vous etes imposable"
    else:
        resultat = "Vous n'etes pas imposable"
    return resultat
print(imposable())