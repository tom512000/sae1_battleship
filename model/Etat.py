# Etat.py
from model.Constantes import *

#
# Définit le type Etat d'une coordonnée d'un bateau et du bateau lui-même.
# Celui-ci est de type str et doit être dans la liste des constantes...
#

# Liste des états
lst_etats_segment_bateau = [const.INTACT, const.TOUCHE]
lst_etats_bateau = lst_etats_segment_bateau + [const.COULE]
lst_resultat_tir = [const.RATE, const.TOUCHE, const.COULE]


def type_etat_segment(etat: str) -> bool:
    """
    Détermine si le paramètre correspond bien à un état d'une case

    :param etat: Chaîne représentant l'état d'une case
    :return: True si il s'agit bien d'un état, False sinon.
    """
    return etat in lst_etats_segment_bateau


# def type_etat_bateau(etat: str) -> bool:
#     """
#     Détermine si le paramètre correspond bien à un état d'un bateau
#
#     :param etat: Chaîne représentant l'état d'un bateau
#     :return: True s'il s'agit bien d'un état, False sinon
#     """
#     return etat in lst_etats_bateau
#

def type_resultat_tir(resultat: str) -> bool:
    """
    Détermine si le paramètre correspond bien à un résultat de tir

    :param resultat: Résultat de tir
    :return: True si c'est un résultat de tir, False sinon
    """
    return resultat in lst_resultat_tir
