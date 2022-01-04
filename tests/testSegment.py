# tests/testSegment.py

import unittest

from model.Segment import *
from model.Constantes import *


class TestSegmentMethods(unittest.TestCase):
    @unittest.skipIf('construireSegment' not in globals(),
                     "Constructeur non écrit")
    def test_construire_segment(self):
        # Test du constructeur sans argument
        s = construireSegment()
        self.assertTrue(type_segment(s), "L'objet construit ne semble pas être un segment...")
        self.assertIsNone(s[const.SEGMENT_COORDONNEES], "Les coordonnées du segment doivent être initialisées à None")
        self.assertEqual(const.INTACT, s[const.SEGMENT_ETAT], "Un segment construit doit être dans l'état intact (const.RATE)")
        # Test du constructeur avec argument
        s = construireSegment((4, 7))
        self.assertTrue(type_segment(s), "L'objet construit ne semble pas être un segment...")
        self.assertTrue(type_coordonnees(s[const.SEGMENT_COORDONNEES]), "Les coordonnées du segment ne sont pas du bon type")
        self.assertEqual((4, 7), s[const.SEGMENT_COORDONNEES],
            f"Les coordonnees du segment devraient être (4, 7) au lieu de {s[const.SEGMENT_COORDONNEES]}")
        self.assertEqual(const.INTACT, s[const.SEGMENT_ETAT], "Un segment construit doit être dans l'état intact (const.RATE)")

    @unittest.skipIf('construireSegment' not in globals() or 'getCoordonneesSegment' not in globals(),
                     "Constructeur ou fonction getCoordonneesSegment non écrit")
    def test_get_coordonnees_segment(self):
        s = construireSegment()
        self.assertIsNone(getCoordonneesSegment(s))
        # On teste si la méthode est robuste contre des appels incorrectes
        self.assertRaises(ValueError, getCoordonneesSegment, "segment")

    @unittest.skipIf('construireSegment' not in globals() or 'getEtatSegment' not in globals(),
                     "Constructeur ou fonction getEtatSegment non écrit")
    def test_get_etat_segment(self):
        s = construireSegment()
        self.assertEqual(const.INTACT, getEtatSegment(s))
        # On teste si la fonction est robuste contre des appels incorrectes
        self.assertRaises(ValueError, getEtatSegment, "segment")

    @unittest.skipIf('construireSegment' not in globals() or 'setCoordonneesSegment' not in globals(),
                     "Constructeur ou fonction setCoordonneesSegment non écrit")
    def test_set_coordonnees_segment(self):
        s = construireSegment()
        setCoordonneesSegment(s, (3, 4))
        self.assertEqual((3, 4), getCoordonneesSegment(s))
        # On teste si la fonction est robuste contre des appels incorrectes
        # Test du premier argument
        self.assertRaises(ValueError, setCoordonneesSegment, "segment", (1, 2))
        # Test du second argument
        self.assertRaises(ValueError, setCoordonneesSegment, s, "blabla")

    @unittest.skipIf('construireSegment' not in globals() or 'setEtatSegment' not in globals(),
                     "Constructeur ou fonction setEtatSegment non écrit")
    def test_set_etat_segment(self):
        s = construireSegment()
        setEtatSegment(s, const.TOUCHE)
        self.assertEqual(const.TOUCHE, getEtatSegment(s))
        # On teste si la fonction est robuste contre des appels incorrectes
        # Test du premier argument
        self.assertRaises(ValueError, setEtatSegment, "segment", const.RATE)
        # Test du second argument
        self.assertRaises(ValueError, setEtatSegment, s, "const.RATE")


