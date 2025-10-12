import unittest
from war.Game import Game
""" import the Game class """


class TestGame(unittest.TestCase):
    def test_initial_mode(self):
        game = Game()
        """create a new Game object"""

        self.assertEqual(game.mode, "")
        """check that game.mode is an empty string after its created"""

    def test_start_runs(self):
        game = Game()
        game.start()
        """call start() to make sure it exists works"""

    def test_pickmode_runs(self):
        game = Game()
        game.pickmode()
        """call pickmode() to make sure it exists and works"""

    def test_cheat_runs(self):
        game = Game()
        game.cheat()
        """Call cheat() to make sure it exists and runs without crashing"""


if __name__ == "__main__":
    unittest.main()
