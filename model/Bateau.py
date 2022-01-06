# Bateau.py

#
# - Définit un bateau sous forme de dictionnaire de la façon suivante :
#   const.BATEAU_NOM : Nom du bateau (voir les constantes dans Constantes.py - clés du dictionnaire const.BATEAUX_CASES)
#   const.BATEAU_SEGMENTS - Liste de listes [coordonnées, état] des segments du bateau.
#       Si le bateau n'est pas positionné, les coordonnées valent None et les états valent const.RATE
#   La taille du bateau n'est pas stockée car elle correspond à la taille de la liste des listes [coordonnées, état]
#

from model.Segment import *
from model.Constantes import *



def type_bateau(bateau: dict) -> bool:
    """
    Détermine si la liste représente un bateau

    :param bateau: Liste représentant un bateau
    :return: <code>True</code> si la liste contient bien un bateau, <code>False</code> sinon.
    """
    return type(bateau) == dict and \
        all([v in bateau for v in [const.BATEAU_NOM, const.BATEAU_SEGMENTS]]) and \
        type(bateau[const.BATEAU_NOM]) == str and \
        bateau[const.BATEAU_NOM] in const.BATEAUX_CASES and type(bateau[const.BATEAU_SEGMENTS]) == list and \
        len(bateau[const.BATEAU_SEGMENTS]) == const.BATEAUX_CASES[bateau[const.BATEAU_NOM]] and \
        all([type_segment(s) for s in bateau[const.BATEAU_SEGMENTS]])


def est_horizontal_bateau(bateau: dict) -> bool:
    """
    Retourne True si le bateau est horizontal, False si il est vertical.

    :param bateau:
    :return: True si le bateau est horizontal, False si il est vertical
    :raise ValueError si le bateau n'est pas placé ou s'il n'est ni vertical, ni horizontal
    """
    if not estPlaceBateau(bateau):
        raise ValueError("est_horizontal_bateau: Le bateau n'est pas positionné")
    pos = getCoordonneesBateau(bateau)
    res = True
    if len(pos) > 1:
        # Horizontal : le numéro de ligne ne change pas
        res = pos[0][0] == pos[1][0]
        # On vérifie que le bateau est toujours horizontal
        for i in range(1, len(pos)):
            if (res and pos[0][0] != pos[i][0]) or (not res and pos[0][1] != pos[i][1]):
                raise ValueError("est_horizontal_bateau: Le bateau n'est ni horizontal, ni vertical ??")
    return res


def construireBateau(nbat: str) -> dict:
    if nbat in const.BATEAUX_CASES:
        bateau = {const.BATEAU_NOM: nbat, const.BATEAU_SEGMENTS: const.BATEAUX_CASES[nbat] * [construireSegment()]}
    else:
        raise ValueError(f"construireBateau: le paramètre {nbat} ne correspond pas à un nom de bateau")
    return bateau


def getNomBateau(bat: dict) -> str:
    if type_bateau(bat) == True:
        ttb = bat[const.BATEAU_NOM]
    else:
        raise ValueError(f"getNomBateau: le paramètre {bat} ne correspond pas à un bateau")
    return ttb


def getTailleBateau(bato: dict) -> int:
    if (type_bateau(bato) == True):
        tba = len(bato[const.BATEAU_SEGMENTS])
    else:
        raise ValueError(f"getTailleBateau: le paramètre {bato} ne correspond pas à un bateau")
    return tba


def getSegmentsBateau(bateau: dict) -> list:
    if (type_bateau(bateau) == True):
        sba = bateau[const.BATEAU_SEGMENTS]
    else:
        raise ValueError(f"getSegmentsBateau: le paramètre {bateau} ne correspond pas à un bateau")
    return sba


def getSegmentBateau(babato: dict, numseg: object) -> list:
    if (type_bateau(babato) == True):
        if type(numseg) == int:
            if (numseg < 0) and (numseg > len(babato[const.BATEAU_SEGMENTS]) - 1):
                test = babato[const.BATEAU_SEGMENTS][numseg]
        elif type(numseg) == tuple:
            bl = False
            for i in babato[const.BATEAU_SEGMENTS]:
                if i[const.SEGMENT_COORDONNEES] == numseg:
                    bl = True
                    test = i
            if bl == False:
                raise ValueError(f"La variable {bl} est encore à False")
        else:
            raise ValueError(f"Le type du second paramètre {type(numseg)} n'est ni un nombre entier ni un tuple")
    else:
        raise ValueError(f"getTailleBateau: le paramètre {babato} ne correspond pas à un bateau")
    return test

"""
def setSegmentBateau(bateau: dict, numseg: int, segment: dict):
    if (type_bateau(bateau) == True):
        if (numseg >= 0) and (numseg <= len(getSegmentsBateau(bateau)) - 1):
            if (type_segment(segment) == True):
                pip = getSegmentsBateau(bateau)
                for i in range(len(pip)):
                    if numseg == i:
                        pip[i] = segment
            else:
                raise ValueError(f"setSegmentBateau: le paramètre {segment} n'est pas de type Segment")
        else:
            raise ValueError(f"Le second paramètre {numseg} n'est pas entre 0 et la taille du bateau -1")
    else:
        raise ValueError(f"setSegmentBateau: le paramètre {bateau} ne correspond pas à un bateau")
    return None
"""

def getCoordoneesBateau(bateau: dict) -> list:
    if type_bateau(bateau) == True:
        listeseg = []
        for i in range(getTailleBateau(bateau)):
            segment = getSegmentBateau(bateau, i)
            listeseg.append(segment[const.SEGMENT_COORDONNEES])
    else:
        raise ValueError(f"getCoordoneesBateau: le paramètre {bateau} ne correspond pas à un bateau")
    return listeseg
