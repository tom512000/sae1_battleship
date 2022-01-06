# Grille.py

from model.Constantes import *
from model.Case import type_case

#
# - Définition de la grille des tirs
#       - tableau 2D (const.DIM x const.DIM) contenant des cases de type type_case.
#
# Bien qu'on pourrait créer une autre grille contenant les bateaux, ceux-ci seront stockés dans une liste
# et chaque bateau contiendra sa liste de coordonnées.
#


def type_grille(g: list) -> bool:
    """
    Détermine si le paramètre est une grille de cases dont le type est passé en paramètre ou non
    :param g: paramètre à tester
    :return: True s'il peut s'agir d'une grille du type voulu, False sinon.
    """
    res = True
    if type(g) != list or len(g) != const.DIM:
        res = False
    else:
        i = 0
        while res and i < len(g):
            res = type(g[i]) == list and len(g[i]) == const.DIM
            j = 0
            while res and j < len(g[i]):
                res = type_case(g[i][j])
                j += 1
            i += 1
    return res


def construireGrille() -> list:
    listegrille = []
    for y in range(const.DIM):
            listegrille.append([None]*const.DIM)
    return listegrille
