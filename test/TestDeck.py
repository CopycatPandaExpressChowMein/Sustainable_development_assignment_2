"""Simple tests for the Deck class."""
import unittest
from war.Deck import Deck
from war.Card import Card

class TestDeck(unittest.TestCase):

    def setUp(self):
        self.deck = Deck()

    def test_deck_has_52_cards(self):
        self.assertEqual(len(self.deck.getDeck()), 52)

    def test_deck_contains_cards(self):
        self.assertTrue(all(isinstance(c, Card) for c in self.deck.getDeck()))

    def test_shuffle_changes_order(self):
        old_order = self.deck.getDeck().copy()
        self.deck.shuffle()
        self.assertNotEqual(old_order, self.deck.getDeck())

    def test_split_half(self):
        half1, half2 = self.deck.split()
        self.assertEqual(len(half1), 26)
        self.assertEqual(len(half2), 26)

if __name__ == '__main__':
    unittest.main()