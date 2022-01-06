# testBateau.py

#
# Classe de tests permettant de tester les fonctions associées aux bateaux
#

import unittest
from model.Bateau import *
from model.Constantes import *
from model.Segment import *
from random import randint, choice, choices


class TestBateauMethods(unittest.TestCase):
    @unittest.skipIf('construireBateau' not in globals(), "Constructeur non écrit")
    def test_construireBateau(self):
        # Création de tous les bateaux
        for nom in const.BATEAUX_CASES:
            b = construireBateau(nom)
            self.assertEqual(2, len(b),f"Le nombre d'éléments devrait être de 3 au lieu de {len(b)}")
            self.assertEqual(nom, b[const.BATEAU_NOM], f"Le nom du bateau devrait être {nom} au lieu de {b[const.BATEAU_NOM]}")
            self.assertEqual(const.BATEAUX_CASES[nom], len(b[const.BATEAU_SEGMENTS]), f"La dimension du navire devrait être {const.BATEAUX_CASES[nom]} au lieu de {b[const.BATEAU_SEGMENTS]}")
            for v in b[const.BATEAU_SEGMENTS]:
                self.assertIsNone(v[const.SEGMENT_COORDONNEES], f"Les coordonnées du bateau ne devraient pas être initialisées")
                self.assertEqual(const.INTACT, v[const.SEGMENT_ETAT], "L'état du bateau devrait être initialis&é à 'const.RATE'")

        # TODO : Vérifier que les exceptions sont au programme !...
        # Création d'un bateau avec un mauvais nom
        self.assertRaises(ValueError, construireBateau, "Un navire quelconque")

    @unittest.skipIf('construireBateau' not in globals() or 'getNomBateau' not in globals(), "Getter sur le nom du bateau non écrit")
    def test_getNomBateau(self):
        # On va tester tous les noms
        for nom in const.BATEAUX_CASES:
            b = construireBateau(nom)
            self.assertEqual(nom, getNomBateau(b), f"Erreur sur la fonction getNomBateau...")
        # Tester la robustesse de la méthode
        self.assertRaises(ValueError, getNomBateau, [ "Autre chose qu'un bateau" ])
        self.assertRaises(ValueError, getNomBateau, "Vraiment autre chose...")

    @unittest.skipIf('construireBateau' not in globals() or 'getTailleBateau' not in globals(), "Getter sur la taille du bateau non écrit")
    def test_getTailleBateau(self):
        # On va tester toutes les tailles de bateau
        for nom in const.BATEAUX_CASES:
            b = construireBateau(nom)
            self.assertEqual(const.BATEAUX_CASES[nom], getTailleBateau(b), f"Erreur sur la fonction getNomBateau...")
        # Tester la robustesse de la méthode
        self.assertRaises(ValueError, getTailleBateau, [ "Autre chose qu'un bateau" ])
        self.assertRaises(ValueError, getTailleBateau, "Vraiment autre chose...")

    @unittest.skipIf('construireBateau' not in globals() or 'getSegmentsBateau' not in globals(),
                     "Getter sur les segments du bateau non écrit")
    def test_getSegmentsBateau(self):
        # On va tester toutes les tailles de bateau
        for nom in const.BATEAUX_CASES:
            b = construireBateau(nom)
            lst = getSegmentsBateau(b)
            self.assertTrue(type(lst) == list, "Ne renvoie pas une liste")
            self.assertEqual(const.BATEAUX_CASES[nom], len(lst), "Le nombre de segments n'est pas correct")
            for n, s in enumerate(lst, start=1) :
                self.assertTrue(type_segment(s), f"Le {n}ième élément de la liste n'est pas un segment")
        # Tester la robustesse de la méthode
        self.assertRaises(ValueError, getSegmentsBateau, [ "Autre chose qu'un bateau" ])
        self.assertRaises(ValueError, getSegmentsBateau, "Vraiment autre chose...")

    @unittest.skipIf('construireBateau' not in globals() or 'getCoordonneesBateau' not in globals(),
                     "Getter sur les coordonnées du bateau non écrit")
    def test_getCoordonneesBateau(self):
        # On va tester toutes les tailles de bateau
        for nom in const.BATEAUX_CASES:
            b = construireBateau(nom)
            lst = getCoordonneesBateau(b)
            self.assertTrue(type(lst) == list, "Ne renvoie pas une liste ?")
            self.assertEqual(const.BATEAUX_CASES[nom], len(lst), "Le nombre de coordonnées n'est pas correct")
            for n, s in enumerate(lst, start=1):
                self.assertTrue(type_coordonnees(s), f"Le {n}ième élément de la liste n'est pas une coordonnée")
        # Tester la robustesse de la méthode
        self.assertRaises(ValueError, getCoordonneesBateau, ["Autre chose qu'un bateau"])
        self.assertRaises(ValueError, getCoordonneesBateau, "Vraiment autre chose...")

    @unittest.skipIf('construireBateau' not in globals() or 'getSegmentBateau' not in globals()
                     or 'setSegmentBateau' not in globals(),
                     "Getter ou Setter sur un segment du bateau non écrit")
    def test_get_setSegmentBateau(self):
        # On va tester toutes les tailles de bateau
        states = [ const.INTACT, const.TOUCHE ]
        for nom in const.BATEAUX_CASES:
            b = construireBateau(nom)
            n = const.BATEAUX_CASES[nom]
            coord = (0, 0)
            for i in range(n):
                s = construireSegment()
                coord = (coord[0] + 1, coord[1])
                setCoordonneesSegment(s, coord)
                etat = choice(states)
                setEtatSegment(s, etat)
                setSegmentBateau(b, i, s)
                # On teste maintenant le segment
                s = getSegmentBateau(b, i)
                self.assertTrue(type_segment(s), "getSegment ne renvoie pas un type segment")
                self.assertEqual(coord, getCoordonneesSegment(s), "Problème avec les coordonnées du segment qui peut provenir de setSegmentBateau ou getSegmentBateau")
                self.assertEqual(etat, getEtatSegment(s), "Problème avec l'état du segment qui peut provenir de getSegmentBateau ou setSegmentBateau")
                # On teste avec les coordonnées
                s = getSegmentBateau(b, coord)
                self.assertTrue(type_segment(s), "getSegment ne renvoie pas un type segment")
                self.assertEqual(coord, getCoordonneesSegment(s),
                                 "Problème avec les coordonnées du segment qui peut provenir de setSegmentBateau ou getSegmentBateau")
                self.assertEqual(etat, getEtatSegment(s),
                                 "Problème avec l'état du segment qui peut provenir de getSegmentBateau ou setSegmentBateau")
                # On teste avec des coordonnées incorrectes
                for i in range(10):
                    c = (randint(0, const.DIM - 1), randint(0, const.DIM - 1))
                    if c not in [ s[const.SEGMENT_COORDONNEES] for s in b[const.BATEAU_SEGMENTS]]:
                        self.assertRaises(ValueError, getSegmentBateau, b, c)

            # Test de la robustesse des getters, setters sur le numéro de segment
            self.assertRaises(ValueError, getSegmentBateau, b, n)
            self.assertRaises(ValueError, setSegmentBateau, b, n, s)
            # Test de la robustesse du setter sur le segment
            self.assertRaises(ValueError, setSegmentBateau, b, 0, [ "Autre chose"])
            self.assertRaises(ValueError, setSegmentBateau, b, 0, "Autre chose")
        # Tester la robustesse des getters, setters sur le premier paramètre de type bateau
        self.assertRaises(ValueError, getSegmentBateau, [ "Autre chose qu'un bateau" ], 0)
        self.assertRaises(ValueError, getSegmentBateau, "Vraiment autre chose...", 0)
        self.assertRaises(ValueError, setSegmentBateau, [ "Autre chose qu'un bateau" ], 0, s)
        self.assertRaises(ValueError, setSegmentBateau, "Vraiment autre chose...", 0, s)

    @unittest.skipIf('construireBateau' not in globals() or 'peutPlacerBateau' not in globals(),
                     "Constructeur ou fonction peutPlacerBateau manquantes")
    def test_peutPlacerBateau(self):
        # On va tester pour tous les bateaux !
        for nom in const.BATEAUX_CASES:
            b = construireBateau(nom)
            # On teste toutes les cases possibles de positionnement
            for i in range(const.DIM - const.BATEAUX_CASES[nom] + 1):
                for j in range(const.DIM - const.BATEAUX_CASES[nom] + 1):
                    self.assertTrue(peutPlacerBateau(b, (i, j), True), f"On peut placer un {nom} en {(i, j)} horizontalement")
                    self.assertTrue(peutPlacerBateau(b, (i, j), False), f"On peut placer un {nom} en {(i, j)} verticalement")
            # Test des positions le long du côté droit
            for i in range(const.DIM):
                for j in range(const.DIM - const.BATEAUX_CASES[nom] + 1, const.DIM):
                    if i <= const.DIM - const.BATEAUX_CASES[nom]:
                        self.assertTrue(peutPlacerBateau(b, (i, j), False), f"On peut placer un {nom} en {(i, j)} verticalement")
                    else:
                        self.assertFalse(peutPlacerBateau(b, (i, j), False), f"On ne peut pas placer un {nom} en {(i, j)} verticalement")
                    self.assertFalse(peutPlacerBateau(b, (i, j), True), f"On ne peut pas placer un {nom} en {(i, j)} horizontalement")
            # Test des positions le long du bord inférieur
            for i in range(const.DIM - const.BATEAUX_CASES[nom] + 1, const.DIM):
                for j in range(const.DIM):
                    if j <= const.DIM - const.BATEAUX_CASES[nom]:
                        self.assertTrue(peutPlacerBateau(b, (i, j), True), f"On peut placer un {nom} en {(i, j)} horizontalement")
                    else:
                        self.assertFalse(peutPlacerBateau(b, (i, j), True), f"On ne peut pas placer un {nom} en {(i, j)} horizontalement")
                    self.assertFalse(peutPlacerBateau(b, (i, j), False), f"On ne peut pas placer un {nom} en {(i, j)} verticalement")
            # Test des positions impossibles
            # Inutile, c'est fait dans type_coordonnees...

    @unittest.skipIf('construireBateau' not in globals() or 'estPlaceBateau' not in globals()
                     or 'setSegmentBateau' not in globals() or 'getTailleBateau' not in globals(),
                     "Une des fonctions construireBateau, estPlaceBateau, setSegmentBateau n'est pas écrite")
    def test_estPlaceBateau(self):
        # Test avec tous les types de bateau
        for nom in const.BATEAUX_CASES:
            # Tests aléatoires...
            for i in range(10):
                b = construireBateau(nom)
                c = (1, 1)
                t = getTailleBateau(b)
                # Modification des segments du bateau
                for j in range(t):
                     setSegmentBateau(b, j, construireSegment(c))
                self.assertTrue(estPlaceBateau(b),
                                f"Le bateau {b} devrait être considéré comme placé, même si les coordonnées sont incohérentes")
                # Choix aléatoire de coordonnées nulles
                nums = choices(list(range(t)), k=randint(1, t))
                for j in nums:
                    setSegmentBateau(b, j, construireSegment())
                self.assertFalse(estPlaceBateau(b),
                                 f"Le bateau {b} ne devrait pas être considéré comme placé")
        # Test des paramètres
        self.assertRaises(ValueError, estPlaceBateau, "N'importe quoi")

    @unittest.skipIf('construireBateau' not in globals() or 'sontVoisinsBateau' not in globals(),
                    "La focntion sontVoisinsBateau n'est pas écrite")
    def test_sontVoisinsBateau(self):
        # On teste avec toutes les combinaisons possibles de bateaux
        for nom1 in const.BATEAUX_CASES:
            b1 = construireBateau(nom1)
            for i in range(getTailleBateau(b1)):
                setSegmentBateau(b1, i, construireSegment((0, 0)))
            for nom2 in const.BATEAUX_CASES:
                b2 = construireBateau(nom2)
                for i in range(getTailleBateau(b2)):
                    setSegmentBateau(b2, i, construireSegment((2, 2)))
                self.assertFalse(sontVoisinsBateau(b1, b2), f"Les bateaux {b1} et {b2} ne sont pas voisins")
                self.assertFalse(sontVoisinsBateau(b2, b1), f"Les bateaux {b1} et {b2} ne sont pas voisins")
                # On insère aléatoirement un segment voisin dans b2
                setSegmentBateau(b2, randint(0, getTailleBateau(b2) - 1), construireSegment((1, 1)))
                self.assertTrue(sontVoisinsBateau(b1, b2), f"Les bateaux {b1} et {b2} ne sont pas voisins")
                self.assertTrue(sontVoisinsBateau(b2, b1), f"Les bateaux {b1} et {b2} ne sont pas voisins")
        # Test des paramètres
        b = construireBateau(const.SOUS_MARIN)
        self.assertRaises(ValueError, sontVoisinsBateau, b, "N'importe quoi")
        self.assertRaises(ValueError, sontVoisinsBateau, "N'importe quoi", b)

    @unittest.skipIf('construireBateau' not in globals() or 'placerBateau' not in globals(),
                     "La fonction placerBateau n'est pas écrite")
    def test_placerBateau(self):
        # On teste tous les bateaux
        for nom in const.BATEAUX_CASES:
            n = const.BATEAUX_CASES[nom]
            b = construireBateau(nom)
            # Test des placements verticaux
            for i in range(const.DIM - n + 1):
                for j in range(const.DIM):
                    placerBateau(b, (i, j), False)
                    pos = [
                        {
                            const.SEGMENT_COORDONNEES: (i + k, j),
                            const.SEGMENT_ETAT: const.INTACT
                        } for k in range(n)
                    ]
                    self.assertEqual(pos, getSegmentsBateau(b))
            # Test des placements horizontaux
            for i in range(const.DIM):
                for j in range(const.DIM - n + 1):
                    placerBateau(b, (i, j), True)
                    pos = [
                        {
                            const.SEGMENT_COORDONNEES: (i, j + k),
                            const.SEGMENT_ETAT: const.INTACT
                        } for k in range(n)
                    ]
                    self.assertEqual(pos, getSegmentsBateau(b))
        # Vérification des paramètres
        self.assertRaises(ValueError, placerBateau, "N'importe quoi", (0, 0), False)
        self.assertRaises(ValueError, placerBateau, construireBateau(const.SOUS_MARIN), "N'importe quoi", False)

    @unittest.skipIf("reinitialiserBateau" not in globals(), "La fonction reinitialiserBateau n'est pas écrite.")
    def test_reinitialiserBateau(self):
        # On teste avec tous les bateaux
        for nom in const.BATEAUX_CASES:
            b = construireBateau(nom)
            "placerBateau(b, (0, 0), True)"
            reinitialiserBateau(b)
            self.assertEqual(construireBateau(nom), b, "Mauvaise réinitialisation")
        # Test des paramètres
        self.assertRaises(ValueError, reinitialiserBateau, "N'importe quoi")

    @unittest.skipIf("contientSegmentBateau" not in globals(), "La fonction 'contientSegmentBateau' n'est pas écrite")
    def test_contientSegmentBateau(self):
        # Test pour tous les bateaux
        for nom in const.BATEAUX_CASES:
            b = construireBateau(nom)
            placerBateau(b, (1, 1), True)
            pos = [(1, 1 + i) for i in range(getTailleBateau(b))]
            for i in range(100):
                p = (randint(0, const.DIM - 1), randint(0, const.DIM - 1))
                self.assertEqual(p in pos, contientSegmentBateau(b, p),
                                 f"Erreur avec {p} pour le bateau {b}")
        # Test des paramètres
        self.assertRaises(ValueError, contientSegmentBateau, "N'importe quoi", (1, 1))
        self.assertRaises(ValueError, contientSegmentBateau, construireBateau(const.TORPILLEUR), "N'importe quoi")

    @unittest.skipIf("setEtatSegmentBateau" not in globals(), "La fonction setEtatSegmentBateau n'est pas écrite.")
    def test_setEtatSegmentBateau(self):
        # Test pour tous les bateaux
        for nom in const.BATEAUX_CASES:
            b = construireBateau(nom)
            placerBateau(b, (1, 0), True)
            pos = getCoordonneesBateau(b)
            for p in pos:
                for etat in [const.INTACT, const.TOUCHE]:
                    setEtatSegmentBateau(b, p, etat)
                    self.assertEqual(etat, getEtatSegment(getSegmentBateau(b, p)),
                                     "Problème dans setEtatSegmentBateau ou getSegmentBateau")
            # Test de robustesse
            for i in range(10):
                c = (randint(0, const.DIM - 1), randint(0, const.DIM - 1))
                if c not in pos:
                    self.assertRaises(ValueError, setEtatSegmentBateau, b, c, etat)
            # Test de robustesse des autres paramètres
            self.assertRaises(ValueError, setEtatSegmentBateau, "N'importe quoi", pos[0], etat)
            self.assertRaises(ValueError, setEtatSegmentBateau, b, "N'importe quoi", etat)
            self.assertRaises(ValueError, setEtatSegmentBateau, b, pos[0], "N'importe quoi")

    @unittest.skipIf("estCouleBateau" not in globals(), "La fonction 'estCouleBateau n'est pas écrite")
    def test_estCouleBateau(self):
        for nom in const.BATEAUX_CASES:
            b = construireBateau(nom)
            placerBateau(b, (0, 0), True)
            pos = getCoordonneesBateau(b)
            self.assertFalse(estCouleBateau(b), f"Le bateau {b} n'est pas coulé.")
            for i in range(len(pos)):
                setEtatSegmentBateau(b, pos[i], const.TOUCHE)
                self.assertEqual(i == len(pos)-1, estCouleBateau(b),
                                 f"Le bateau {b} coulé : {i == len(pos) - 1}")
            # Test de la robustesse des paramètres
            self.assertRaises(ValueError, estCouleBateau, "N'importe quoi")

