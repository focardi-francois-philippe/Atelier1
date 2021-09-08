import datetime as date
from typing import AsyncGenerator

def saisieInformation():
    ANNEEMINIMUMDEPERMIS = 2
    age = int(input("Quel age avec vous ? "))
    anneeOptentionPermis = int(input("En quel annee avec vous obtenue votre permis"))
    accident = input("Avez vous deja eu des accidents taper O pour oui N pour non")
    nombreAccident = 0
    tempsDePermis = 0
    tempsDansLaCompanie = 0
    TARIF = ("Refus","Bleu","Vert","Orange","Rouge")
    tarifDestine = None
    if(accident == "O" or accident == "o"):
        nombreAccident = int(input("Combien d'accident? "))
    tempsDePermis = date.date.today().year - anneeOptentionPermis
    
    if(age<25):
        if(tempsDePermis<ANNEEMINIMUMDEPERMIS):
            if(nombreAccident == 0):
                tarifDestine = TARIF[4]
            else:
                tarifDestine = TARIF[0]
        elif(tempsDePermis>ANNEEMINIMUMDEPERMIS):
            if(nombreAccident == 0):
                tarifDestine = TARIF[3]
            elif(nombreAccident == 1):
                tarifDestine = TARIF[4]
            else:
                tarifDestine = TARIF[0]
    elif(age>25):
        if(tempsDePermis<ANNEEMINIMUMDEPERMIS):
            if(nombreAccident == 0):
                    tarifDestine = TARIF[3]
            elif(nombreAccident == 1):
                tarifDestine = TARIF[4]  
            else:
                tarifDestine = TARIF[0] 
        else:
            if(nombreAccident ==0):
                tarifDestine = TARIF[2]
            elif(nombreAccident == 1):
                tarifDestine = TARIF[3]
            elif (nombreAccident == 2):
                tarifDestine = TARIF[4]
            else:
                tarifDestine = TARIF[0]
    return tarifDestine    
               
print(saisieInformation())
            
             
    
            
            
                
            
    