# testJoueur.py

#
# Classe de tests permettant de tester les fonctions associées aux joueurs
#

import unittest

from model.Constantes import *
from model.Joueur import *
from model.Bateau import *
from random import randint, choices, choice


class TestJoueurMethods(unittest.TestCase):

    @unittest.skipIf("construireJoueur" not in globals(), "Le constructeur de Joueur n'est pas défini")
    def test_construire_joueur(self):
        j = ["Machin", [], "truc"]
        self.assertFalse(type_joueur(j))
        j = construireJoueur("Moi", list(const.BATEAUX_CASES.keys()))
        self.assertTrue(type_joueur(j))

    @unittest.skipIf("construireJoueur" not in globals() or "getNomJoueur" not in globals(),
                     "Le constructeur ou le getter sur le nom du joueur ne sont pas écrits")
    def test_getNomJoueur(self):
        j = construireJoueur("Moi", [])
        self.assertEqual("Moi", getNomJoueur(j), "Problème sur le getter du nom")
        j = construireJoueur("Toi", [])
        self.assertEqual("Toi", getNomJoueur(j), "Problème sur le getter du nom")
        # Test des paramètres
        self.assertRaises(ValueError, getNomJoueur, "Autre chose")

    @unittest.skipIf("construireJoueur" not in globals() or "getNombreBateauxJoueur" not in globals(),
                     "Le constructeur ou le getter sur le nombre de bateaux du joueur ne sont pas écrits")
    def test_getNomBreBateauxJoueur(self):
        lst = list(const.BATEAUX_CASES.keys())
        for i in range(10):
            nb = randint(0, 10)
            j = construireJoueur("Toi", choices(lst, k=nb))
            self.assertEqual(nb, getNombreBateauxJoueur(j), "Problème sur le getter du nombre de bateaux")
        # Test des paramètres
        self.assertRaises(ValueError, getNombreBateauxJoueur, "Autre chose")

    @unittest.skipIf("construireJoueur" not in globals() or "getBateauxJoueur" not in globals(),
                     "Le constructeur ou le getter sur les bateaux du joueur ne sont pas écrits")
    def test_getBateauxJoueur(self):
        lst = list(const.BATEAUX_CASES.keys())
        for i in range(10):
            nb = randint(0, 5)
            lst_b = choices(lst, k=nb)
            attendu = [{const.BATEAU_NOM: n,
                    const.BATEAU_SEGMENTS: [{const.SEGMENT_COORDONNEES: None, const.SEGMENT_ETAT: const.INTACT}
                                            for i in range(const.BATEAUX_CASES[n])]} for n in lst_b]
            attendu = sorted(attendu, key=lambda d: d[const.BATEAU_NOM])
            j = construireJoueur("Toi", lst_b)
            res = sorted(getBateauxJoueur(j), key=lambda d: d[const.BATEAU_NOM])
            self.assertEqual(attendu, res, "Problème sur le getter des bateaux du joueur")
        # Test des paramètres
        self.assertRaises(ValueError, getBateauxJoueur, "Autre chose")

    @unittest.skipIf("construireJoueur" not in globals() or "getGrilleTirsJoueur" not in globals(),
                     "Le constructeur ou le getter sur la grille de tirs du joueur ne sont pas écrits")
    def test_getGrilleTirsJoueur(self):
        j = construireJoueur("Toi", [])
        self.assertTrue(type_grille(getGrilleTirsJoueur(j)), "Problème sur le getter de la grille du joueur")
        # Test des paramètres
        self.assertRaises(ValueError, getGrilleTirsJoueur, "Autre chose")

    @unittest.skipIf("construireJoueur" not in globals() or "getGrilleTirsJoueur" not in globals()
                     or "getGrilleTirsAdversaire" not in globals(),
                     "Le constructeur ou un des getters sur les grilles de tirs ne sont pas écrits")
    def test_getGrilleTirsAdversaire(self):
        j = construireJoueur("Toi", [])
        # Test destructif pour vérifier que les getters ne renvoient pas la même liste
        lst1 = getGrilleTirsJoueur(j)
        lst2 = getGrilleTirsAdversaire(j)
        lst1.clear()
        self.assertFalse(len(lst2) == 0, "les deux getters renvoient la même grille !?")
        self.assertTrue(type_grille(lst2), "Problème sur le getter de la grille de l'adversaire")
        # Test des paramètres
        self.assertRaises(ValueError, getGrilleTirsAdversaire, "Autre chose")

    @unittest.skipIf("placerBateauJoueur" not in globals(), "La fonction 'placerBateauJoueur' n'est pas écrite")
    def test_placerBateauJoueur(self):
        # Cas école : on place deux bateaux, un cuirassé et un torpilleur
        j = construireJoueur("Test", [const.CUIRASSE, const.TORPILLEUR])
        lst_bateaux = getBateauxJoueur(j)
        idx_c = 0 if getNomBateau(lst_bateaux[0]) == const.CUIRASSE else 1
        idx_t = 1 if idx_c == 0 else 1
        # On place le cuirasse horizontalement sur la seconde ligne, seconde colonne
        placerBateau(lst_bateaux[idx_c], (1, 1), True)
        # On tente de placer le torpilleur verticalement sur les premières colonnes
        for li in range(3):
            for co in range(getTailleBateau(lst_bateaux[idx_c]) + 2):
                self.assertFalse(placerBateauJoueur(j, lst_bateaux[idx_t], (li, co), False))
        # On place maintenant le torpilleur à une position correcte
        self.assertTrue(placerBateauJoueur(j, lst_bateaux[idx_t], (3, 0), True))
        # On vérifie les coordonnées du torpilleur
        attendu = {const.BATEAU_NOM: const.TORPILLEUR,
                   const.BATEAU_SEGMENTS:
                       [construireSegment((3, i)) for i in range(getTailleBateau(lst_bateaux[idx_t]))]}
        self.assertEqual(attendu, lst_bateaux[idx_t], "Mauvais placement du torpilleur ???")
        # Test des paramètres
        self.assertRaises(ValueError, placerBateauJoueur, "N'importe quoi", lst_bateaux[idx_t], (0, 0), True)
        self.assertRaises(ValueError, placerBateauJoueur, j, "N'importe quoi", (0, 0), True)
        self.assertRaises(ValueError, placerBateauJoueur, j, lst_bateaux[idx_t], "N'importe quoi", True)
        # Test du bateau n'appartenant pas au joueur
        self.assertRaises(RuntimeError, placerBateauJoueur, j, construireBateau(const.TORPILLEUR), (0, 0), True)

    @unittest.skipIf("reinitialiserBateauxJoueur" not in globals(),
                     "La fonction reinitialiserBateauxJoueur n'est pas écrite")
    def test_reinitialiserBateauxJoueur(self):
        # On teste avec une flotte simple
        noms = [ const.PORTE_AVION, const.CUIRASSE, const.TORPILLEUR]
        j = construireJoueur("Test", noms)
        lst_bateaux = getBateauxJoueur(j)
        # Placement des bateaux
        for li in range(len(lst_bateaux)):
            placerBateauJoueur(j, lst_bateaux[li], (2*li, 0), True)
        reinitialiserBateauxJoueur(j)
        # On permet que les bateaux soient réalloués
        lst_bateaux = getBateauxJoueur(j)
        for b in lst_bateaux:
            self.assertEqual(construireBateau(getNomBateau(b)), b, "Erreur dans la réinitialisation des bateaux")
        # Test des paramètres
        self.assertRaises(ValueError, reinitialiserBateauxJoueur, "N'importe quoi")

    @unittest.skipIf('estPerdantJoueur' not in globals(), "La fonction estPerdantJoueur n'est pas écrite")
    def test_estPerdantJoueur(self):
        j = construireJoueur("Test", [const.CUIRASSE, const.TORPILLEUR, const.PORTE_AVION])
        self.assertFalse(estPerdantJoueur(j))
        lst_b = getBateauxJoueur(j)
        # On marque aléatoirement 10 fois les bateaux
        for _ in range(10):
            # On marque tous les bateaux comme coulés
            for i, b in enumerate(lst_b):
                placerBateau(b, (2*i, 0), True)
                for ii in range(getTailleBateau(b)):
                    setEtatSegmentBateau(b, getCoordonneesBateau(b)[ii], const.TOUCHE)
            self.assertTrue(estPerdantJoueur(j))
            # On choisit aléatoirement un bateau
            b = choice(lst_b)
            # On choisit aléatoirement un segment du bateau
            n_s = randint(0, getTailleBateau(b) - 1)
            setEtatSegmentBateau(b, getCoordonneesBateau(b)[n_s], const.INTACT)
            self.assertFalse(estPerdantJoueur(j))
            # On réinitialise tous les bateaux
            reinitialiserBateauxJoueur(j)
        # Test du paramètre
        self.assertRaises(ValueError, estPerdantJoueur, "N'importe quoi")
