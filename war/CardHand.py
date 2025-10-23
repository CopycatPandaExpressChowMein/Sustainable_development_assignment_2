"""CardHand class for managing a player's hand of cards."""

from Card import Card  # Import Card class from the same package


class CardHand:
    def __init__(self, cards):
        """
        Initialize the hand with a list of cards.
        :param cards: list of Card objects
        """
        self.hand = list(cards)  # All cards currently in hand
        self.activeCard = []  # Cards that have been drawn (active)
        self.amount = len(self.hand)  # Number of cards currently in hand

    def drawcard(self):
        """
        Draw one card from the hand.
        Moves the card from 'hand' to 'activeCard'.
        :return: Card object or None if hand is empty
        """
        if not self.hand:
            return None  # No cards left to draw
        card = self.hand.pop(0)  # Remove the top card from the hand
        self.activeCard.append(card)  # Add it to active cards
        self.amount = len(self.hand)  # Update the count
        return card

    def addCard(self, card):
        """
        Add one card to the hand.
        :param card: Card object
        """
        self.hand.append(card)  # Add the card to the hand
        self.amount = len(self.hand)  # Update the count

    def removeCard(self):
        """
        Remove and return one active card.
        :return: Card object or None if no active cards
        """
        if not self.activeCard:
            return None
        return self.activeCard.pop(0)  # Remove and return one active card

    def getHand(self):
        """
        Return the current list of cards in hand.
        :return: list of Card objects
        """
        return self.hand

    def setHand(self, hand):
        """
        Replace the hand with a new list of cards.
        :param hand: list of Card objects
        """
        self.hand = list(hand)  # Set a new hand
        self.amount = len(hand)  # Update the count
