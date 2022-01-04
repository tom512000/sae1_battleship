# tests/testGrille.py

#
# Classe de tests permettant de tester la construction d'une grille
#
import unittest
from model.Grille import *


class TestGrille(unittest.TestCase):

    @unittest.skipIf("construireGrille" not in globals(), "Le constructeur de la grille n'est pas défini")
    def test_construire_grille(self):
        grille = construireGrille()
        self.assertTrue(type_grille(grille), "La grille construite ne correspond pas au 'type' attendu")
