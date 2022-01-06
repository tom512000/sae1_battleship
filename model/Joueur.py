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
        nbbatjoueur = len(joueur[const.JOUEUR_LISTE_BATEAUX])
    else:
        raise ValueError(f"getNombreBateauxJoueur: le paramètre {joueur} ne correspond pas à un joueur")
    return nbbatjoueur


def getBateauxJoueur(joueur: dict) -> list:
    if type_joueur(joueur) == True:
        listebatjoueur = joueur[const.JOUEUR_LISTE_BATEAUX]
    else:
        raise ValueError(f"getBateauxJoueur: le paramètre {joueur} ne correspond pas à un joueur")
    return listebatjoueur


def getGrilleTirsJoueur(joueur: dict) -> list:
    if type_joueur(joueur) == True:
        grtirsjoueur = joueur[const.JOUEUR_GRILLE_TIRS]
    else:
        raise ValueError(f"getGrilleTirsJoueur: le paramètre {joueur} ne correspond pas à un joueur")
    return grtirsjoueur


def getGrilleTirsAdversaire(joueur: dict) -> list:
    if type_joueur(joueur) == True:
        grtirsadvers = joueur[const.JOUEUR_GRILLE_ADVERSAIRE]
    else:
        raise ValueError(f"getGrilleTirsAdversaire: le paramètre {joueur} ne correspond pas à un joueur")
    return grtirsadvers

"""
def placerBateauJoueur(joueur: dict, bateau: dict, coord: tuple, position: bool) -> bool:
    if type_joueur(joueur) == True:
        if type_bateau(bateau) == True:
            if type_coordonnees(coord) == True:
                if bateau not in getBateauxJoueur(joueur):
                    raise RuntimeError(f"placerBateauJoueur: le paramètre {bateau} n'appartient pas au joueur {joueur}")
                else:
                    test = peutPlacerBateau(bateau, coord, position)
                    if test == True:
                        res = True
                    elif test == False:
                        res = True
            else:
                raise ValueError(f"placerBateauJoueur: le paramètre {coord} ne correspond pas à des coordonnées")
        else:
            raise ValueError(f"placerBateauJoueur: le paramètre {bateau} ne correspond pas à un bateau")
    else:
        raise ValueError(f"placerBateauJoueur: le paramètre {joueur} ne correspond pas à un joueur")
    return res
"""


def reinitialiserBateauxJoueur(joueur: dict):
    if type_joueur(joueur) == True:
        for test in getBateauxJoueur(joueur):
            reinitialiserBateau(test)
    else:
        raise ValueError(f"reinitialiserBateauxJoueur: le paramètre {joueur} ne correspond pas à un joueur")
    return None
