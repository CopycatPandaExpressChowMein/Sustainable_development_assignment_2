import unittest
from war.Intelligance import Intelligance

class TestIntelligance(unittest.TestCase):
    """ Tests for Intelligance class """

    def test_initial_hand(self):
        """ AI hand should initially be None """
        ai = Intelligance()
        self.assertIsNone(ai.hand)

    def test_name_set_and_get(self):
        """ AI name should be set and get properly """
        ai = Intelligance("Bot")
        self.assertEqual(ai.getName(), "Bot")

    def test_set_and_get_hand(self):
        """ Can set and get the hand """
        ai = Intelligance()
        fake_hand = object()
        ai.setHand(fake_hand)
        self.assertEqual(ai.getHand(), fake_hand)

if __name__ == "__main__":
    unittest.main()
