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
        self.assertEqual(len(self.hand.get_hand()), 3)
        self.assertEqual(self.hand.amount, 3)

    def test_draw_card(self):
        """Test drawing a card from the hand."""
        drawn = self.hand.draw_card()
        self.assertEqual(drawn, self.card1)
        self.assertEqual(len(self.hand.get_hand()), 2)
        self.assertIn(drawn, self.hand.activeCard)

    def test_draw_card_empty(self):
        """Test drawing from an empty hand returns None."""
        empty_hand = CardHand([])
        self.assertIsNone(empty_hand.draw_card())

    def test_add_card(self):
        """Test adding a new card to the hand."""
        new_card = Card(7, "🂧", "Clubs", "black")
        self.hand.add_card(new_card)
        self.assertIn(new_card, self.hand.get_hand())
        self.assertEqual(self.hand.amount, 4)

    def test_remove_card(self):
        """Test removing an active card."""
        self.hand.draw_card()  # move one card to active
        removed = self.hand.remove_card()
        self.assertEqual(removed, self.card1)
        self.assertEqual(len(self.hand.activeCard), 0)

    def test_get_hand(self):
        """Test getting the hand list."""
        hand_list = self.hand.get_hand()
        self.assertEqual(len(hand_list), 3)
        self.assertIn(self.card2, hand_list)

    def test_set_hand(self):
        """Test replacing the hand."""
        new_cards = [self.card1]
        self.hand.set_hand(new_cards)
        self.assertEqual(len(self.hand.get_hand()), 1)
        self.assertEqual(self.hand.amount, 1)

    def test_return_cards_moves_active_back(self):
        """Active cards should be returned to hand when return_cards is called."""
        # draw two cards into active
        self.hand.draw_card()
        self.hand.draw_card()
        active_before = list(self.hand.get_active_card())
        self.hand.return_cards()
        self.assertEqual(len(self.hand.get_active_card()), 0)
        self.assertEqual(self.hand.amount, 3)
        # ensure previously active cards are now back in hand
        for c in active_before:
            self.assertIn(c, self.hand.get_hand())

    def test_set_active_card_and_remove(self):
        """set_active_card should replace active cards and remove_card should pop from it."""
        self.hand.set_active_card([self.card3])
        self.assertEqual(self.hand.get_active_card(), [self.card3])
        removed = self.hand.remove_card()
        self.assertEqual(removed, self.card3)
        self.assertEqual(len(self.hand.get_active_card()), 0)

    def test_get_and_set_amount(self):
        """get_amount should return current amount and set_amount should update it."""
        # initial amount set in setUp
        self.assertEqual(self.hand.get_amount(), 3)
        # set a new amount and verify getter reflects it
        new_amount = 42
        returned = self.hand.set_amount(new_amount)
        self.assertEqual(returned, new_amount)
        self.assertEqual(self.hand.get_amount(), new_amount)


if __name__ == "__main__":
    unittest.main()
