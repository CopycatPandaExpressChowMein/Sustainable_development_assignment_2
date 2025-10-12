import unittest
from war.Intelligance import Intelligance
"""Import the Intelligance class"""


class TestIntelligance(unittest.TestCase):
    def test_initial_hand(self):
        ai = Intelligance()
        """creats a intelligance object """

        self.assertIsNone(ai.hand)
        """chekc that ai hand is None"""


if __name__ == "__main__":
    unittest.main()
