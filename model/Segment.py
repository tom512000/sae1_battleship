# model/Segment.py

from model.Coordonnees import *
from model.Etat import *
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


def construireSegment(coord: tuple = None) -> dict:
    if type_coordonnees(coord) == True:
        seg = {const.SEGMENT_COORDONNEES: coord, const.SEGMENT_ETAT: const.INTACT}
    else:
        raise ValueError(f"construireSegment: le paramètre {coord} ne correspond pas à des coordonnées")
    return seg


def getCoordonneesSegment(typseg: dict) -> tuple:
    if (type_segment(typseg) == True):
        coo = typseg[const.SEGMENT_COORDONNEES]
    else:
        raise ValueError(f"getCoordonneesSegment: le paramètre {typseg} n'est pas de type Segment")
    return coo


def getEtatSegment(etaseg: dict) -> tuple:
    if (type_segment(etaseg) == True):
        etat = etaseg[const.SEGMENT_ETAT]
    else:
        raise ValueError(f"getEtatSegment: le paramètre {etaseg} n'est pas de type Segment")
    return etat


def setCoordonneesSegment(dictio: dict, coordonnees: tuple):
    if (type_segment(dictio) == True):
        if (type_coordonnees(coordonnees) == True):
            dictio[const.SEGMENT_COORDONNEES] = coordonnees
        else:
            raise ValueError(f"setCoordonneesSegment: le paramètre {coordonnees} ne correspond pas à des coordonnées")
    else:
        raise ValueError(f"setCoordonneesSegment: le paramètre {dictio} n'est pas de type Segment")
    return None
