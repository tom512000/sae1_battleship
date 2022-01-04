# view/__init__.py
#
#  Permet d'initialiser la fenêtre principale
#

from view.BattleCanvas import BattleCanvas


print(dir())
if 'TESTS' not in dir():
    window = BattleCanvas()
