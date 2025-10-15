import unittest
from war.Game import Game



class TestGame(unittest.TestCase):
    """ Tests for Game logic """

    def test_initial_mode(self):
        """ Game should initialize with the correct mode """
        game = Game()
        self.assertEqual(game.mode, "You against AI")

    def test_start_runs(self):
        """ Game start runs without crashing """
        game = Game()
        game.start()

    def test_pickmode_runs(self):
        """ Pickmode prints mode info """
        game = Game()
        game.pickmode()

    def test_cheat_runs(self):
        """ Cheat method runs without crashing """
        game = Game()
        game.cheat()

if __name__ == "__main__":
    unittest.main()
