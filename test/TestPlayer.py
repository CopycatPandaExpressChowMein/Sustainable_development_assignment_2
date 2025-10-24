"""Unit tests for the Player class and basic player behaviours."""

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

    def test_multiple_players_independent(self):
        """Changing one player's name or hand shouldn't affect another."""
        p1 = Player("Alice", CardHand())
        p2 = Player("Bob", CardHand())
        self.assertEqual(p1.get_name(), "Alice")
        self.assertEqual(p2.get_name(), "Bob")
        p1.set_name("Alicia")
        self.assertEqual(p1.get_name(), "Alicia")
        self.assertEqual(p2.get_name(), "Bob")
        # set hands independently
        h1 = CardHand()
        h2 = CardHand()
        p1.set_hand(h1)
        p2.set_hand(h2)
        self.assertIs(p1.get_hand(), h1)
        self.assertIs(p2.get_hand(), h2)

    def test_str_contains_expected_tokens(self):
        """Player.__str__ should include 'Player:' and 'Hand:' and the player name."""
        p = Player("Charlie", CardHand())
        s = str(p)
        self.assertIn("Player:", s)
        self.assertIn("Hand:", s)
        self.assertIn("Charlie", s)

    def test_set_hand_returns_value_and_allows_mutation(self):
        """set_hand should return the same object and Player.get_hand should reflect mutations."""
        p = Player("D", CardHand())
        new_hand = CardHand()
        ret = p.set_hand(new_hand)
        self.assertIs(ret, new_hand)
        # mutate the hand and check player.view
        new_hand.addCard(object())
        self.assertIs(p.get_hand(), new_hand)

    def test_set_name_returns_and_updates(self):
        """set_name should return the new name and update get_name()."""
        p = Player("OldName", CardHand())
        ret = p.set_name("NewName")
        self.assertEqual(ret, "NewName")
        self.assertEqual(p.get_name(), "NewName")


if __name__ == "__main__":
    unittest.main()
