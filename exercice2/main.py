def reconaissance_de_caractere():
    """Fonction permettant de determiner si un caractere entrer et un nombre majuscules ou bien minuscule"""
    caractereChoisis = input("Veuillez entrer un caractere ") # saisie utilisateur
    if(caractereChoisis >= '0' and caractereChoisis <='9'):
        print("C'est un chiffre ")
    elif(caractereChoisis >= 'A' and caractereChoisis <= 'Z'):
        print("C'est une lettre majuscule ")
    elif(caractereChoisis >= 'a' and caractereChoisis <= 'z'):
        print("C'est une lettre minuscule ")
    else:
        print("c'est un caractere speciale ")
    
reconaissance_de_caractere()