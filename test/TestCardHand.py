"""Unit tests for the CardHand class."""
import unittest
from war.Card import Card
from war.CardHand import CardHand

class TestCardHand(unittest.TestCase):

    def setUp(self):
        """Set up a sample hand with a few cards."""
        self.card1 = Card(3, "🂣", "Spades", "black")
        self.card2 = Card(5, "🂥", "Hearts", "red")
        self.card3 = Card(10, "🂪", "Diamonds", "red")
        self.hand = CardHand([self.card1, self.card2, self.card3])

    def test_initial_hand_size(self):
        """Test if hand initializes correctly with given cards."""
        self.assertEqual(len(self.hand.getHand()), 3)
        self.assertEqual(self.hand.amount, 3)

    def test_drawcard(self):
        """Test drawing a card from the hand."""
        drawn = self.hand.drawcard()
        self.assertEqual(drawn, self.card1)
        self.assertEqual(len(self.hand.getHand()), 2)
        self.assertIn(drawn, self.hand.activeCard)

    def test_drawcard_empty(self):
        """Test drawing from an empty hand returns None."""
        empty_hand = CardHand([])
        self.assertIsNone(empty_hand.drawcard())

    def test_addCard(self):
        """Test adding a new card to the hand."""
        new_card = Card(7, "🂧", "Clubs", "black")
        self.hand.addCard(new_card)
        self.assertIn(new_card, self.hand.getHand())
        self.assertEqual(self.hand.amount, 4)

    def test_removeCard(self):
        """Test removing an active card."""
        self.hand.drawcard()  # move one card to active
        removed = self.hand.removeCard()
        self.assertEqual(removed, self.card1)
        self.assertEqual(len(self.hand.activeCard), 0)

    def test_getHand(self):
        """Test getting the hand list."""
        hand_list = self.hand.getHand()
        self.assertEqual(len(hand_list), 3)
        self.assertIn(self.card2, hand_list)

    def test_setHand(self):
        """Test replacing the hand."""
        new_cards = [self.card1]
        self.hand.setHand(new_cards)
        self.assertEqual(len(self.hand.getHand()), 1)
        self.assertEqual(self.hand.amount, 1)

    def test_return_cards_moves_active_back(self):
        """Active cards should be returned to hand when return_cards is called."""
        # draw two cards into active
        self.hand.drawcard()
        self.hand.drawcard()
        active_before = list(self.hand.get_active_card())
        self.hand.return_cards()
        self.assertEqual(len(self.hand.get_active_card()), 0)
        self.assertEqual(self.hand.amount, 3)
        # ensure previously active cards are now back in hand
        for c in active_before:
            self.assertIn(c, self.hand.getHand())

    def test_set_active_card_and_remove(self):
        """set_active_card should replace active cards and removeCard should pop from it."""
        self.hand.set_active_card([self.card3])
        self.assertEqual(self.hand.get_active_card(), [self.card3])
        removed = self.hand.removeCard()
        self.assertEqual(removed, self.card3)
        self.assertEqual(len(self.hand.get_active_card()), 0)

if __name__ == '__main__':
    unittest.main()
