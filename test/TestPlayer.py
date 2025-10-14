import unittest
from war.Player import Player


class TestPlayer(unittest.TestCase):
        
    def test_set_name(self):
        player = Player()
        self.assertEqual(player.set_name("John"), "John")

    def test_set_hand(self):
        player = Player()
        self.assertEqual(player.set_hand(object), object)

    def test_get_name(self):
        player = Player("John")
        self.assertEqual(player.get_name(), "John")

    def test_get_hand(self):
        player = Player("John", object)
        self.assertEqual(player.get_hand(), object)


if __name__ == "__main__":
    unittest.main()
