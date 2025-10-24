"""Unit tests for AI behaviour (Intelligence class)."""
import unittest

from war.Intelligence import Intelligence


class TestIntelligence(unittest.TestCase):
    """Tests for Intelligence class"""

    def test_initial_hand(self):
        """AI hand should initially be None"""
        ai = Intelligence()
        self.assertIsNone(ai.get_hand())

    def test_name_set_and_get(self):
        """AI name should be set and get properly"""
        ai = Intelligence("Bot")
        self.assertEqual(ai.get_name(), "Bot")

    def test_set_and_get_hand(self):
        """Can set and get the hand"""
        ai = Intelligence()
        fake_hand = object()
        ai.set_hand(fake_hand)
        self.assertEqual(ai.get_hand(), fake_hand)

    def test_default_name_is_AI(self):
        """Default AI name should be 'AI' when not provided."""
        ai = Intelligence()
        self.assertEqual(ai.get_name(), "AI")

    def test_set_name_changes_name(self):
        """Setting the AI name should update the stored name."""
        ai = Intelligence()
        ai.set_name("Bot")
        self.assertEqual(ai.get_name(), "Bot")

    def test_choose_index_empty_hand_returns_none(self):
        """choose_index should return None when hand is empty or None."""
        ai = Intelligence(level="random")
        ai.set_hand(None)
        self.assertIsNone(ai.choose_index())
        # empty hand object
        class Empty:
            def getHand(self):
                return []
        ai.set_hand(Empty())
        self.assertIsNone(ai.choose_index())

    def test_set_level_fallback_and_top(self):
        """Unknown level falls back to 'top'; top returns index 0."""
        ai = Intelligence(level="unknown")
        self.assertEqual(ai.get_level(), 'top')
        # fake hand with two cards
        from war.Card import Card
        class FakeHand:
            def __init__(self, cards):
                self._cards = cards
            def getHand(self):
                return list(self._cards)
        cards = [Card(3, '3', 'H', 'red'), Card(5, '5', 'D', 'black')]
        ai.set_hand(FakeHand(cards))
        ai.set_level('top')
        self.assertEqual(ai.choose_index(), 0)

    def test_choose_index_random_and_greedy(self):
        """Test choose_index for random (within range) and greedy (chooses highest value)."""
        from war.Card import Card

        # random level: index should be within valid range
        ai = Intelligence(level="random")
        # create a fake hand with three cards
        class FakeHand:
            def __init__(self, cards):
                self._cards = cards
            def getHand(self):
                return list(self._cards)

        cards = [Card(2, '2', 'Hearts', 'red'), Card(14, 'A', 'Spades', 'black'), Card(10, '10', 'Clubs', 'black')]
        ai.set_hand(FakeHand(cards))
        idx = ai.choose_index()
        self.assertIn(idx, (0, 1, 2))

        # greedy should pick the Ace (value 14) at index 1
        ai.set_level("greedy")
        idx2 = ai.choose_index()
        self.assertEqual(idx2, 1)

    def test_set_and_get_level_values(self):
        """Setting levels should be reflected by get_level()."""
        ai = Intelligence()
        for lvl in ("top", "random", "greedy"):
            ai.set_level(lvl)
            self.assertEqual(ai.get_level(), lvl)

    def test_greedy_chooses_first_of_ties(self):
        """Greedy should choose the first occurrence when multiple cards tie for highest value."""
        from war.Card import Card
        class FakeHand:
            def __init__(self, cards):
                self._cards = cards
            def getHand(self):
                return list(self._cards)

        cards = [Card(10, '10', 'H', 'red'), Card(10, '10', 'D', 'black')]
        ai = Intelligence(level="greedy")
        ai.set_hand(FakeHand(cards))
        self.assertEqual(ai.choose_index(), 0)

    def test_random_choice_within_bounds_on_multiple_calls(self):
        """Random choice should always produce indices within the valid range."""
        from war.Card import Card
        class FakeHand:
            def __init__(self, cards):
                self._cards = cards
            def getHand(self):
                return list(self._cards)

        cards = [Card(i, str(i), 'S', 'black') for i in range(5)]
        ai = Intelligence(level="random")
        ai.set_hand(FakeHand(cards))
        for _ in range(20):
            idx = ai.choose_index()
            self.assertIn(idx, range(5))


if __name__ == "__main__":
    unittest.main()
