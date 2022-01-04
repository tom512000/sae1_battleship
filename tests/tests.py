import unittest
import sys

sys.path.insert(0, "..")

# Inclusion des tests à effectuer

from testSegment import TestSegmentMethods
from testBateau import TestBateauMethods
from testCoordonnee import TestCoordonneesMethods
from testJoueur import TestJoueurMethods
from testGrille import TestGrille

if __name__ == '__main__':
    unittest.main()

