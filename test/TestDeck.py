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

    def test_deck_unique_symbols(self):
        """Ensure all cards in deck have unique symbols (52 unique glyphs)."""
        symbols = [c.get_symbol() for c in self.deck.getDeck()]
        self.assertEqual(len(symbols), 52)
        self.assertEqual(len(set(symbols)), 52)

    def test_split_returns_all_cards(self):
        """The union of halves should equal the original deck set."""
        d = list(self.deck.getDeck())
        half1, half2 = self.deck.split()
        combined = half1 + half2
        self.assertEqual(len(combined), len(d))
        # ensure same multiset of symbols
        self.assertEqual(sorted([c.get_symbol() for c in combined]), sorted([c.get_symbol() for c in d]))

    def test_shuffle_variation_over_multiple_runs(self):
        """Shuffling multiple times should produce at least some order changes (probabilistic but reliable here)."""
        d1 = [c.get_symbol() for c in self.deck.getDeck()]
        self.deck.shuffle()
        d2 = [c.get_symbol() for c in self.deck.getDeck()]
        # very unlikely to be equal after shuffle
        self.assertNotEqual(d1, d2)

    def test_getDeck_returns_list_reference(self):
        """Modifying the returned list should reflect in the Deck object (intent of current implementation)."""
        dref = self.deck.getDeck()
        self.assertIsInstance(dref, list)
        first = dref[0]
        # swap first two elements and ensure deck reflects change
        dref[0], dref[1] = dref[1], dref[0]
        self.assertNotEqual(self.deck.getDeck()[0], first)

if __name__ == '__main__':
    unittest.main()
