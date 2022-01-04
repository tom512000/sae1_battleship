# testCoordonnee.py

#
# Classe de tests permettant de tester les fonctions associées aux coordonnées
#

import unittest
from random import randint
from model.Coordonnees import *
from model.Constantes import *


class TestCoordonneesMethods(unittest.TestCase):
    @unittest.skipIf("sontVoisins" not in globals(), "La fonction 'sontVoisins' n'est pas écrite")
    def test_sontVoisins(self):
        dep_max = const.DIM//2
        for i in range(1000):
            # Choix aléatoire d'une case
            c1 = (randint(0, const.DIM - 1), randint(0, const.DIM - 1))
            # Choix d'un déplacement aléatoire
            dep = (randint(-dep_max, dep_max), randint(-dep_max, dep_max))
            attendu = dep in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
            c2 = (c1[0] + dep[0], c1[1] + dep[1])
            if type_coordonnees(c2):
                self.assertEqual(attendu, sontVoisins(c1, c2),
                                 f"Les cases {c1} et {c2} sont considérées comme " + ("" if attendu else "non")
                                 + " voisines")
        # Test de la validité des paramètres
        self.assertRaises(ValueError, sontVoisins, "n'importe quoi", (1, 1))
        self.assertRaises(ValueError, sontVoisins, (1, 1), "n'importe quoi")
        self.assertRaises(ValueError, sontVoisins, (1, 1), None)
        self.assertRaises(ValueError, sontVoisins, None, (1, 1))
