# Coordonnees.py

#
# - Définit les coordonnées d'une case
#
#  Une coordonnée est un tuple de deux entiers compris entre 0 (inclus) et const.DIM (exclus)
#  Elle peut aussi être None si elle est non définie
#

from model.Constantes import *


def type_coordonnees(c: tuple) -> bool:
    """
    Détermine si le tuple correspond à des coordonnées
    Les coordonnées sont sous la forme (ligne, colonne).
    Malheureusement, il n'est pas possible de tester si une inversion est faite entre ligne et colonne...

    :param c: coordonnées
    :return: True s'il s'agit bien de coordonnées, False sinon
    """
    return c is None or (type(c) == tuple and len(c) == 2 and 0 <= c[0] < const.DIM and 0 <= c[1] < const.DIM)


def sontVoisins(coord1: tuple, coord2: tuple) -> bool:
    vraimentvoisin = False
    if not type_coordonnees(coord1) or coord1 is None:
        raise ValueError(f"sontVoisins : Le paramètre {coord1} ne correspond pas à des coordonnées")
    if not type_coordonnees(coord2) or coord2 is None:
        raise ValueError(f"sontVoisins : Le paramètre {coord2} n'est pas valide")
    for x in range(-1, 2, 1):
        for y in range(-1, 2, 1):
            test = (coord1[0] + x, coord1[1] + y)
            if test != coord1:
                if test == coord2:
                    vraimentvoisin = True
    return vraimentvoisin


