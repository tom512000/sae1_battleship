# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import pygame

from view import window

from model.Constantes import *
from model.Joueur import *

def main_test():
    j = construireJoueur("Test", [const.PORTE_AVION, const.CUIRASSE, const.CROISEUR, const.TORPILLEUR])
    # j = construireJoueur("Test", [const.PORTE_AVION, const.CUIRASSE])
    view.window.afficher(j)
    view.window.placer_bateaux()
    view.window.set_action("Pour terminer, cliquez dans la grille de DROITE")
    view.window.get_clicked_cell(2)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main_test()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
