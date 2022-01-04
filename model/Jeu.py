# model/Jeu.py

#
#  Module mettant en place les joueurs
#
from model.Joueur import type_joueur
from model.Constantes import *

# Pour jouer, un joueur doit être capable de :
# - placer ses bateaux
# - choisir une case pour tirer
# - traiter le résultat d'un tir
# Pour cela, on crée un acteur : dictionnaire
#       const.ACTEUR : Joueur (voir construireJoueur)
#       const.ACTEUR_PLACER_BATEAUX : fonction permettant de placer les bateaux
#       const.ACTEUR_CHOISIR_CASE : fonction permettant de choisir la case où le tir aura lieu
#       const.ACTEUR_TRAITER_RESULTAT : fonction permettant de traiter le résultat d'un précédent tir

def type_acteur(agent: dict) -> bool:
    """
    Détermine si le tuple passé en paramètre peut être un agent ou non
    :param agent: Agent à tester
    :return: True si c'est un agent, False sinon
    """
    return type(agent) == dict and \
        all(k in agent for k in [const.ACTEUR,
                                 const.ACTEUR_PLACER_BATEAUX,
                                 const.ACTEUR_CHOISIR_CASE,
                                 const.ACTEUR_TRAITER_RESULTAT]) and \
        type_joueur(agent[const.ACTEUR]) and \
        callable(agent[const.ACTEUR_PLACER_BATEAUX]) and callable(agent[const.ACTEUR_CHOISIR_CASE]) and \
        callable(agent[const.ACTEUR_TRAITER_RESULTAT])


