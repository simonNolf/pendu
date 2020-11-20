def verification(proposition,mot_a_trouver):
    resultat=0
    for lettre in mot_a_trouver:
        if proposition in mot_a_trouver:
            return True
        else:
           return False

def remplacement(mot_a_trouver,chaine_lettres_trouvees):
     mot_crypte = ""
     for lettre in mot_a_trouver:
        if lettre in chaine_lettres_trouvees:
            mot_crypte += lettre
        else:
            mot_crypte += "*"
     return mot_crypte


def potence (nombre_de_vie):
    if nombre_de_vie==8:
        print("Il te reste encore toutes tes vies:")
        print (nombre_de_vie)
        return  ("""
                  _________
                  |/     |
                  |     
                  |
                  |
                 /|

                                 """)
    if nombre_de_vie==7:
        print("Dommage tu viens de perdre ta première vie:",nombre_de_vie,) 
        return("""
                 _________
                 |/     |
                 |      0
                 |
                 |
                /|
                           """) 

    if nombre_de_vie==6:
        print("Doucement,a cette vitesse tu ne vas plus avoir de vies:",nombre_de_vie,) 
        return("""
                 _________
                 |/     |
                 |      0
                 |      |
                 |
                /|   
                           """)
 
    if nombre_de_vie==5:
        print("Aïe, tu as perdu une troisième vie:",nombre_de_vie,)
        return("""    
                 _________
                 |/     | 
                 |      0
                 |     /|
                 |
                /|
                           """)


    if nombre_de_vie==4:
        print("tu as déjà perdu la moitier de tes vies:",nombre_de_vie,)
        return ("""
                 _________
                 |/     |
                 |      0
                 |     /|>
                 |
                /|
                           """)


    if nombre_de_vie==3:
        print("Plus que 3 vies, attention:",nombre_de_vie,)
        return ("""        
                 _________
                 |/     |
                 |      0
                 |     /|>
                 |     /
                /|
                           """)


    if nombre_de_vie==2:
        print("Réfléchis bien aux lettres que tu vas proposer, il ne te reste plus que 2 vies:",nombre_de_vie,)
        return ("""
                 _________
                 |/     |
                 |      0
                 |     /|>
                 |     / >
                /|
                            """)



    if nombre_de_vie==1:
        print("Mmm, fais attention il ne te reste qu une vie:",nombre_de_vie,)
        return ("""
                 _________
                 |/     |
                 |      0
                 |     /|>
                 |     / >  
                /|    *****        
                     *******
                                    """)
    



 

   












