import unittest
from war.Intelligence import Intelligence


class TestIntelligence(unittest.TestCase):
    """Tests for Intelligance class"""

    def test_initial_hand(self):
        """AI hand should initially be None"""
        ai = Intelligence()
        self.assertIsNone(ai.hand)

    def test_name_set_and_get(self):
        """AI name should be set and get properly"""
        ai = Intelligence("Bot")
        self.assertEqual(ai.getName(), "Bot")

    def test_set_and_get_hand(self):
        """Can set and get the hand"""
        ai = Intelligence()
        fake_hand = object()
        ai.setHand(fake_hand)
        self.assertEqual(ai.getHand(), fake_hand)


if __name__ == "__main__":
    unittest.main()
