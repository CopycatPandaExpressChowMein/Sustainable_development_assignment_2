"""Simple unit tests for the Deck class.

This module tests the core functionality of the Deck class, including:
- Ensuring the deck contains 52 cards
- Verifying that all items are instances of the Card class
- Checking that shuffling changes the card order
- Confirming that the deck splits evenly between two players
"""

import unittest
from war.Deck import Deck
from war.Card import Card


class TestDeck(unittest.TestCase):
    """Unit tests for the Deck class."""

    def setUp(self):
        """Set up a new Deck instance before each test."""
        self.deck = Deck()

    def test_deck_has_52_cards(self):
        """Ensure that the deck contains exactly 52 cards."""
        self.assertEqual(len(self.deck.getDeck()), 52)

    def test_deck_contains_cards(self):
        """Verify that every item in the deck is a Card object."""
        self.assertTrue(all(isinstance(c, Card) for c in self.deck.getDeck()))

    def test_shuffle_changes_order(self):
        """Ensure that shuffling the deck changes the card order."""
        old_order = self.deck.getDeck().copy()
        self.deck.shuffle()
        self.assertNotEqual(old_order, self.deck.getDeck())

    def test_split_half(self):
        """Verify that the deck splits evenly into two halves of 26 cards."""
        half1, half2 = self.deck.split()
        self.assertEqual(len(half1), 26)
        self.assertEqual(len(half2), 26)


if __name__ == '__main__':
    unittest.main()
