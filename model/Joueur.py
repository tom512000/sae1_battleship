# Joueur.py

from model.Bateau import *
from model.Grille import *
from model.Constantes import *

#
# Un joueur est représenté par un dictionnaire contenant les couples (clé, valeur) suivants :
#  const.JOUEUR_NOM : Nom du joueur de type str
#  const.JOUEUR_LISTE_BATEAUX : Liste des bateaux du joueur
#  const.JOUEUR_GRILLE_TIRS : Grille des tirs sur les bateaux adverses
#  const.JOUEUR_GRILLE_ADVERSAIRE : une grille des tirs de l'adversaire pour tester la fonction de tir
#  de l'adversaire.
#


def type_joueur(joueur: dict) -> bool:
    """
    Retourne <code>True</code> si la liste semble correspondre à un joueur,
    <code>false</code> sinon.

    :param joueur: Dictionnaire représentant un joueur
    :return: <code>True</code> si le dictionnaire représente un joueur, <code>False</code> sinon.
    """
    return type(joueur) == dict and len(joueur) >= 4 and \
        len([p for p in [ const.JOUEUR_NOM, const.JOUEUR_LISTE_BATEAUX, const.JOUEUR_GRILLE_TIRS] if p not in joueur]) == 0 and \
        type(joueur[const.JOUEUR_NOM]) == str and type(joueur[const.JOUEUR_LISTE_BATEAUX]) == list \
        and type_grille(joueur[const.JOUEUR_GRILLE_TIRS]) \
        and all(type_bateau(v) for v in joueur[const.JOUEUR_LISTE_BATEAUX])


def construireJoueur(nom: str, nombat: list) -> dict:
    joueurbat = []
    for i in range(len(nombat)):
        joueurbat = joueurbat + [construireBateau(nombat[i])]
    joueurgr = construireGrille()
    adversgr = construireGrille()
    joueur = {const.JOUEUR_NOM: nom,
              const.JOUEUR_LISTE_BATEAUX: joueurbat,
              const.JOUEUR_GRILLE_TIRS: joueurgr,
              const.JOUEUR_GRILLE_ADVERSAIRE: adversgr}

    return joueur


def getNomJoueur(joueur: dict) -> str:
    if type_joueur(joueur) == True:
        nomjoueur = joueur[const.JOUEUR_NOM]
    else:
        raise ValueError(f"getNomJoueur: le paramètre {joueur} ne correspond pas à un joueur")
    return nomjoueur


def getNombreBateauxJoueur(joueur: dict) -> list:
    if type_joueur(joueur) == True:
        listebatjoueur = len(joueur[const.JOUEUR_LISTE_BATEAUX])
    else:
        raise ValueError(f"getNombreBateauxJoueur: le paramètre {joueur} ne correspond pas à un joueur")
    return listebatjoueur


