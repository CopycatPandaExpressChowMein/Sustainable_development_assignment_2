"""Unit tests for the Deck class."""

import unittest
from war.Deck import Deck
from war.Card import Card


class TestDeck(unittest.TestCase):
    """Unit tests for the Deck class and its methods."""

    def setUp(self):
        """Create a fresh deck before each test."""
        self.deck = Deck()

    def test_create_returns_52_cards(self):
        """Test that create() produces exactly 52 Card objects."""
        cards = self.deck.create()
        self.assertEqual(len(cards), 52)
        self.assertTrue(all(isinstance(card, Card) for card in cards))

    def test_shuffle_changes_order(self):
        """Test that shuffle() changes the card order."""
        original_order = self.deck.getDeck().copy()
        self.deck.shuffle()
        self.assertNotEqual(original_order, self.deck.getDeck(), "Deck order did not change after shuffle.")

    def test_split_returns_two_equal_halves(self):
        """Test that split() returns two equal halves of 26 cards each."""
        half1, half2 = self.deck.split()
        self.assertEqual(len(half1), 26)
        self.assertEqual(len(half2), 26)

    def test_getDeck_returns_list_of_cards(self):
        """Test that getDeck() returns a list of Card objects."""
        deck_list = self.deck.getDeck()
        self.assertIsInstance(deck_list, list)
        self.assertTrue(all(isinstance(card, Card) for card in deck_list))

    def test_setDeck_replaces_deck(self):
        """Test that setDeck() replaces the deck with a new one."""
        new_cards = [Card(2, "🂢", "Spades", "black"), Card(3, "🂣", "Spades", "black")]
        self.deck.setDeck(new_cards)
        self.assertEqual(self.deck.getDeck(), new_cards)
        self.assertEqual(len(self.deck.getDeck()), 2)


if __name__ == "__main__":
    unittest.main()

