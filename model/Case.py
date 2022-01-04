# Case.py
from model.Constantes import *
from model.Etat import type_resultat_tir

#
# Définition d'une case d'une grille
#
# Description de la grille de tirs, l'état d'une case peut être :
#    - None : aucun tir
#    - const.RATE : Tir dans l'eau
#    - const.TOUCHE : Bateau touché
#    - const.COULE : Bateau coulé


def type_case(c: object) -> bool:
    """
    Détermine si le paramètre correspond à une case d'une grille de tir

    :param c: paramètre dont on veut connaître le type
    :return: True si c'est un type d'une case de grille de tir, False sinon
    """
    return c is None or type_resultat_tir(c)
