def election():
    "Fonction permettant de determiner quel candidat est elu"
    NOMBREDECANDIDATS = 4
    ScoreDesCandidats = list(map(float,input("Entrez le score des candidats chacun separer d'espaces ").split(" ")))
    x=1
    premierCandidat = ScoreDesCandidats[0]
    CandidatPresentAuxSecondTour = []
    nombreDeCandidatPresentSecondTour = 0
    candidatAvecPlusDe50 = False
    premierCandidatFavorable = True
    
    if(premierCandidat>=50):
        return "Candidat Elu"
    if(premierCandidat < 12.5):
        return "candidat battut"
    while(x<NOMBREDECANDIDATS):
        if(ScoreDesCandidats[x]>=50):
            candidatAvecPlusDe50 = True
            return "Candidat Battut"
        
        
        if(ScoreDesCandidats[x] > 12.5):
            CandidatPresentAuxSecondTour.append(ScoreDesCandidats[x])
        x+=1
    nombreDeCandidatPresentSecondTour = len(CandidatPresentAuxSecondTour)
    x = 1
    
    while(x < nombreDeCandidatPresentSecondTour):
        if(premierCandidat < CandidatPresentAuxSecondTour[x]):
            premierCandidatFavorable = False
        x+=1

    if(premierCandidatFavorable):
        return "le candidat est en balotage favorable"
    
    return "le candidat est en balotage defavorable"
    
print(election())