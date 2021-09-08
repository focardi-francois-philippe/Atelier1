def reprographie():
    """Fonction permettant de determiner la somme de la facture en fonction d'un nombre de photocopie"""
    nombreDePhotocopie = int(input("Entrez le nombre de photocopie a effectuer "))
    PREMIER_PRIX = 0.10
    DEUXIEME_PRIX = 0.09
    TROISIEME_PRIX = 0.08
    PREMIERE_TRANCHE = 10
    DEUXIEME_TRANCHE = 20
    TROISIEME_TRANCHE = 30
    resultat = 0
    if(nombreDePhotocopie>TROISIEME_TRANCHE):
        resultat = DEUXIEME_TRANCHE*DEUXIEME_PRIX+1+(nombreDePhotocopie-30)*TROISIEME_PRIX
    elif(nombreDePhotocopie<=TROISIEME_TRANCHE):
        if(nombreDePhotocopie/10>1):
            resultat = (nombreDePhotocopie-10)*DEUXIEME_PRIX+(PREMIERE_TRANCHE*PREMIER_PRIX)
        else:
            resultat = nombreDePhotocopie*PREMIER_PRIX
    return resultat
print(reprographie())
    