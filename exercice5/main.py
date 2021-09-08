def calculDeFraisPortuaire():
    """Fonction permettant de calculer les portuaires apres plusieurs 
    entrer de l'utilisateur (nom voilier,longueur,catagegorie)
    """
    TARIFMENSUEL1 = 100
    TARIFMENSUEL2 = 200
    TARIFMENSUEL3 = 400
    TARIFMENSUEL4 = 600
    TAXESPECIALEANNUELLEVOILIERCATEGORIE1 = 100
    TAXESPECIALEANNUELLEVOILIERCATEGORIE2 = 150
    TAXESPECIALEANNUELLEVOILIERCATEGORIE3 = 250
    
    coutMensuel = 0
    coutAnnuel = 0
    taxeSpecialeAnnuelle = 0
    nomDuVoilier = input("ENTREZ le nom du voilier: ")
    longueur = float(input("Entrez la longueur du voilier: "))
    categorie = int(input("Entrez la categorie du voilier 1 2 ou 3 : "))
    
    if(longueur<5):
        coutMensuel = TARIFMENSUEL1
    elif(longueur<=10):
        coutMensuel = TARIFMENSUEL2
    elif(longueur<=12):
        coutMensuel = TARIFMENSUEL3
    else:
        coutMensuel = TARIFMENSUEL4
    
    if(categorie==1):
        taxeSpecialeAnnuelle = TAXESPECIALEANNUELLEVOILIERCATEGORIE1
    elif(categorie==2):
        taxeSpecialeAnnuelle = TAXESPECIALEANNUELLEVOILIERCATEGORIE2
    elif(categorie==3):
        taxeSpecialeAnnuelle = TAXESPECIALEANNUELLEVOILIERCATEGORIE3
        
    coutAnnuel = taxeSpecialeAnnuelle+coutMensuel*12
    
    return "le coût annuel d’une place au port pour le voilier "+nomDuVoilier+" est de "+ str(coutAnnuel)+" euros"
print(calculDeFraisPortuaire());   
  
    
    