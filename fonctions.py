def verification(proposition, mot_a_trouver):
    for lettre in mot_a_trouver:
        if proposition in mot_a_trouver:
            return True
        else:
            return False


def remplacement(mot_a_trouver, chaine_lettres_trouvees):
    mot_crypte = ""
    for lettre in mot_a_trouver:
        if lettre in chaine_lettres_trouvees:
            mot_crypte += lettre
        else:
            mot_crypte += "*"
    return mot_crypte


def potence(nombre_de_vie):
    if nombre_de_vie == 8:
        print("Il te reste encore toutes tes vies:")
        print(nombre_de_vie)
        return ("""
                  _________
                  |/     |
                  |     
                  |
                  |
                 /|

                                 """)
    if nombre_de_vie == 7:
        print("Dommage tu viens de perdre ta première vie:", nombre_de_vie, )
        return ("""
                 _________
                 |/     |
                 |      0
                 |
                 |
                /|
                           """)

    if nombre_de_vie == 6:
        print("Doucement,a cette vitesse tu ne vas plus avoir de vies:", nombre_de_vie, )
        return ("""
                 _________
                 |/     |
                 |      0
                 |      |
                 |
                /|   
                           """)

    if nombre_de_vie == 5:
        print("Aïe, tu as perdu une troisième vie:", nombre_de_vie, )
        return ("""    
                 _________
                 |/     | 
                 |      0
                 |     /|
                 |
                /|
                           """)

    if nombre_de_vie == 4:
        print("tu as déjà perdu la moitier de tes vies:", nombre_de_vie, )
        return ("""
                 _________
                 |/     |
                 |      0
                 |     /|>
                 |
                /|
                           """)

    if nombre_de_vie == 3:
        print("Plus que 3 vies, attention:", nombre_de_vie, )
        return ("""        
                 _________
                 |/     |
                 |      0
                 |     /|>
                 |     /
                /|
                           """)

    if nombre_de_vie == 2:
        print("Réfléchis bien aux lettres que tu vas proposer, il ne te reste plus que 2 vies:", nombre_de_vie, )
        return ("""
                 _________
                 |/     |
                 |      0
                 |     /|>
                 |     / >
                /|
                            """)

    if nombre_de_vie == 1:
        print("Mmm, fais attention il ne te reste qu une vie:", nombre_de_vie, )
        return ("""
                 _________
                 |/     |
                 |      0
                 |     /|>
                 |     / >  
                /|    *****        
                     *******
                                    """)

zoo = {"tigre", "gorille", "lion"}
aliment = {"poire", "oignon", "melon"}
class Zoo:
    def __init__(self, nom=""):
        self._nom = zoo

    def nom(self):
        return self._nom


class Aliment:
    def __init__(self, nom=""):
        self._nom = aliment

    def nom(self):
        return self._nom


class User:
    pass


def interface_console(choix_utilisateur):
    print("Bonjour,bienvenue sur le jeu de pendu by Nathan & Simon")
    print("veuillez-vous inscrire si ce n'est pas déja fait")
    nombre_de_vie = 8
    mot_crypte = ""
    catégorie = input("veuillez choisir la catégorie de votre mot entre 'zoo' et 'aliment")
    if catégorie == "zoo":
        liste_mots = random.choice(Zoo.nom())
    if catégorie == "aliment":
        liste_mots = random.choice(Aliment.nom())
    mot_a_trouver = random.choice(liste_mots)
    chaine_lettres_eronnees = []
    chaine_lettres_trouvees = []
    mot_trouve = remplacement(mot_a_trouver, chaine_lettres_trouvees)
    print("Voici le mot à trouver : {0}".format(mot_trouve))
    while mot_trouve != mot_a_trouver and nombre_de_vie > 0:
        proposition = input("Propose une lettre qui pourrais se trouver dans le mot:")
        for lettre in chaine_lettres_trouvees:
            if proposition == lettre in chaine_lettres_trouvees:
                print("Tu as dèjà proposé cette lettre")
            for lettre in chaine_lettres_eronnees:
                if proposition == lettre in chaine_lettres_eronnees:
                    print("Tu as déjà proposé cette lettre")
        if verification(proposition, mot_a_trouver):
            chaine_lettres_trouvees += proposition
        print(remplacement(mot_a_trouver, chaine_lettres_trouvees))
        elif proposition == lettre in chaine_lettres_eronnees:
        nombre_de_vie = nombre_de_vie
        else:
        chaine_lettres_eronnees.append(proposition)
        nombre_de_vie -= 1
    print(potence(nombre_de_vie))
    mot_trouve = remplacement(mot_a_trouver, chaine_lettres_trouvees)

    if mot_trouve == mot_a_trouver:
        print("Bravo,tu as trouvé le mot:")
    elif nombre_de_vie == 0:
        print("Dommage, tu feras mieux la prochaine fois")
