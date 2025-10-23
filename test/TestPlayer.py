import unittest
from war.Player import Player
from war.CardHand import CardHand


class TestPlayer(unittest.TestCase):

    def setUp(self):
        """Sets up an empty player and cardHand object before tests begin."""
        self.player = Player()
        self.hand = CardHand()

    def test_set_name(self):
        """Checks whether the set_name function correctly sets the player name."""
        self.assertEqual(self.player.set_name("John"), "John")
    
    def test_set_hand(self):
        """Checks whether the set_hand function correctly sets the player hand."""
        self.assertEqual(self.player.set_hand(self.hand), self.hand)
    
    def test_get_name(self):
        """Checks whether the get_name function correctly returns the player name."""
        self.assertEqual(self.player.get_name(), "John")
    
    def test_get_hand(self):
        """Checks whether the get_hanf function correctly returns the players cardhand."""
        self.assertEqual(self.player.get_hand(), self.hand)

if __name__ == "__main__":
    unittest.main()
