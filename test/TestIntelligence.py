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


if __name__ == "__main__":
    unittest.main()
