# Constantes.py

#
# Définition des constantes utilisées dans ce module
#
import const

#
# Définition des résultats du tir
#
const.RATE = "Dans l'eau"
const.INTACT = "Intact"
const.TOUCHE = "Touché"
const.COULE = "Coulé"
const.FOND = "Fond"

#
# Dimension de la grille de la bataille navale
#
const.DIM = 10

#
# Definition des bateaux et de leurs images
#
# Navire de 5 cases
const.PORTE_AVION = "Porte-avion"

# Navire de 4 cases
const.CUIRASSE = "Cuirassé"

# Navire de 3 cases
const.CROISEUR = "Croiseur"

# Navire de 2 cases
const.TORPILLEUR = "Torpilleur"

# Navire d'1 case
const.SOUS_MARIN = "Sous-marin"

# Dictionnaire des navires associés au nombre de cases qu'ils occupent
const.BATEAUX_CASES = {
    const.PORTE_AVION: 5,
    const.CUIRASSE: 4,
    const.CROISEUR: 3,
    const.TORPILLEUR: 2,
    const.SOUS_MARIN: 1
}

# Constantes concernant le bateau
const.BATEAU_NOM = "Nom du bateau"
const.BATEAU_SEGMENTS = "Segments du bateau"

# Constantes concernant un segment de bateau
const.SEGMENT_COORDONNEES = "Coordonnées du segment"
const.SEGMENT_ETAT = "Etat du segment"

# Constantes concernant l'agent
const.ACTEUR = "Joueur"
const.ACTEUR_PLACER_BATEAUX = "Placer les bateaux"
const.ACTEUR_CHOISIR_CASE = "Choisir une case"
const.ACTEUR_TRAITER_RESULTAT = "Traiter le résultat"

# Constantes concernant le joueur
const.JOUEUR_NOM = "Nom du joueur"
const.JOUEUR_LISTE_BATEAUX = "Liste des bateaux"
const.JOUEUR_GRILLE_TIRS = "Grille des tirs"
const.JOUEUR_GRILLE_ADVERSAIRE = "Grille des tirs de l'adversaire"


