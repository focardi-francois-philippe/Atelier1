def calcul_frais_mensuel_vehicule():
    """fonction permettant de calculer les frais mensuel en fonction du type de vehicule"""
    NOMBREDELITRESDEREFERENCEPOURCYLINDRESUPEIREURA2000KM = 10
    NOMBREDELITRESDEREFERENCEPOURCYLINDREINFERIEURA2000KMETDIESEL = 8
    FRAISENTRETIENSDIESEL = 1.70
    FRAISENTRETIENSESSENCE = 1.50
    NOMBREDEKILOMETRESPARDEFAUT = 100
    nombreDeKmClientAnnuel = int(input("Combien de kilometre parcourez vous en une année ? "))
    typeDeCarburant = input("Quel type de carburant disposez vous ? (E pour essence D pour diesel)")
    cylindreDeLaVoiture = int(input("quel est la taille de la voiture ?"))
    coutDuCarburant = float(input("Prix du carburant ? "))
    
    
    nombreDeKmClientMensuel = nombreDeKmClientAnnuel/12
  
    nombreDeLitres = 0
    coutMensuel = 0
    
    if(typeDeCarburant == "E"):
        if(cylindreDeLaVoiture >= 2000):
            nombreDeLitres = (nombreDeKmClientMensuel/NOMBREDEKILOMETRESPARDEFAUT)*NOMBREDELITRESDEREFERENCEPOURCYLINDRESUPEIREURA2000KM
            coutMensuel = nombreDeLitres*coutDuCarburant*FRAISENTRETIENSESSENCE
        elif(cylindreDeLaVoiture < 2000):
            nombreDeLitres = (nombreDeKmClientMensuel/NOMBREDEKILOMETRESPARDEFAUT)*NOMBREDELITRESDEREFERENCEPOURCYLINDREINFERIEURA2000KMETDIESEL
            coutMensuel = nombreDeLitres*coutDuCarburant*FRAISENTRETIENSESSENCE
    elif(typeDeCarburant == "D"):
        nombreDeLitres = (nombreDeKmClientMensuel/NOMBREDEKILOMETRESPARDEFAUT)*NOMBREDELITRESDEREFERENCEPOURCYLINDREINFERIEURA2000KMETDIESEL
        coutMensuel = nombreDeLitres*coutDuCarburant*FRAISENTRETIENSDIESEL
    return str(coutMensuel) + "€"
       
print(calcul_frais_mensuel_vehicule())