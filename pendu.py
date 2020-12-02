from fonctions import *
import random

print("Bonjour,bienvenue sur le jeu de pendu by Nathan & Simon")
print("veuillez-vous inscrire si ce n'est pas déja fait")
print("quel est/sera votre pseudo?")
user= input("votre nom d'utilisateur")
log = open("user.txt", "a")
for nom in log:
    if
nombre_de_vie = 8
mot_crypte = ""
liste_mots = ["banane", "arbre", "coque", "travail", "machine", "python", "programme", "abeille",
              "anticonstitutionnellement",
              "némotechnique", "hydrophobe", "Ornithorynque", "telecommande", "Halloween", "Hirondelles",
              "Indépendence", "poulet",
              "couscous", "dorum", "champignons", "eau", "chameau", "telephone", "velo"]
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
    if verification(proposition, mot_a_trouver):from
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