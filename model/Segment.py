# model/Segment.py

from model.Coordonnees import type_coordonnees
from model.Etat import type_etat_segment
from model.Constantes import *

#
# définit un segment de bateau :
# Un segment de bateau est un dictionnaire contenant les couples (clé, valeur) suivants :
#   - const.SEGMENT_COORDONNEES : Les coordonnées du segment sur la grille
#   - ccnst.SEGMENT_ETAT : L'état du segment (const.RATE ou const.TOUCHE)
#


def type_segment(objet: dict) -> bool:
    """
    Détermine si l'objet passé en paramètre peut être interprété ou non
    comme un segment de bateau.

    :param objet: Objet à analyser
    :return: True si l'objet peut correspondre à un segment
    False sinon.
    """
    return type(objet) == dict and \
           all([k in objet for k in [const.SEGMENT_COORDONNEES, const.SEGMENT_ETAT]]) \
           and type_coordonnees(objet[const.SEGMENT_COORDONNEES]) \
           and type_etat_segment(objet[const.SEGMENT_ETAT])


