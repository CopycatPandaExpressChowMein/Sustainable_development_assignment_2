import unittest
from war.Player import Player
from war.CardHand import CardHand


class TestPlayer(unittest.TestCase):

    def setUp(self):
        """Sets up an empty player and cardHand object before tests begin."""
        self.hand = CardHand()
        self.player = Player("John", self.hand)
        

    def test_set_name(self):
        """Checks whether the set_name function correctly sets the player name to a new value."""
        self.assertEqual(self.player.set_name("Abigail"), "Abigail")
    
    def test_set_hand(self):
        """Checks whether the set_hand function correctly sets the player hand to a new value."""
        new_hand = CardHand()
        self.assertEqual(self.player.set_hand(new_hand), new_hand)
    
    def test_get_name(self):
        """Checks whether the get_name function correctly returns the player name."""
        self.assertEqual(self.player.get_name(), "John")
    
    def test_get_hand(self):
        """Checks whether the get_hand function correctly returns the players cardhand."""
        self.assertEqual(self.player.get_hand(), self.hand)

    def test_default_name_and_str(self):
        """Default player has name 'Anonymous' and __str__ includes the name."""
        p = Player()
        self.assertEqual(p.get_name(), "Anonymous")
        s = str(p)
        self.assertIn("Player:", s)
        self.assertIn(p.get_name(), s)

    def test_set_hand_none_allowed(self):
        """Setting hand to None should be allowed and return None."""
        p = Player("X", None)
        self.assertIsNone(p.get_hand())

if __name__ == "__main__":
    unittest.main()
