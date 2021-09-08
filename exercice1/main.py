def calcul_Salaire():
    """Calcul le salaire a partir d'un nombre d'heure de travail et le salaire horaire"""
    salaireHoraire = 10 #definition du taux horraire
    nombreHeureTravail = 250 #definition du nombre d'heure de travail
    salaireMensuel = nombreHeureTravail * salaireHoraire #calcul du salaire mensuel
    if(nombreHeureTravail>160):
        salaireMensuel = salaireMensuel + (1.25*salaireHoraire-salaireHoraire)*(nombreHeureTravail-160) #majoration a 25%
        if(nombreHeureTravail>200):
            salaireMensuel += (1.50*salaireHoraire-salaireHoraire)*(nombreHeureTravail-200) #majoration a 50%
        
    return salaireMensuel

print(calcul_Salaire())
        
    