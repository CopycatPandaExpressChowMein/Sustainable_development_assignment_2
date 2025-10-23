"""Unit tests for the Card class."""
import unittest
from war.Card import Card  # Import from your package

class TestCard(unittest.TestCase):

    def setUp(self):
        """Set up a sample card for testing."""
        self.card = Card(3, "🂣", "Spades", "black")

    def test_get_value(self):
        """Test getting card value."""
        self.assertEqual(self.card.get_value(), 3)

    def test_get_symbol(self):
        """Test getting card symbol."""
        self.assertEqual(self.card.get_symbol(), "🂣")

    def test_get_suit(self):
        """Test getting card suit."""
        self.assertEqual(self.card.get_suit(), "Spades")

    def test_get_color(self):
        """Test getting card color."""
        self.assertEqual(self.card.get_color(), "black")

    def test_set_value(self):
        """Test setting card value."""
        self.card.set_value(10)
        self.assertEqual(self.card.get_value(), 10)

    def test_set_symbol(self):
        """Test setting card symbol."""
        self.card.set_symbol("🂩")
        self.assertEqual(self.card.get_symbol(), "🂩")

    def test_set_suit(self):
        """Test setting card suit."""
        self.card.set_suit("Hearts")
        self.assertEqual(self.card.get_suit(), "Hearts")

    def test_set_color(self):
        """Test setting card color."""
        self.card.set_color("red")
        self.assertEqual(self.card.get_color(), "red")

if __name__ == '__main__':
    unittest.main()
