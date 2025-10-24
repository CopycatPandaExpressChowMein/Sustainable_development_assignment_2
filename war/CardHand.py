"""CardHand class for managing a player's hand of cards."""

class CardHand:
    def __init__(self, cards=[]):
        """
        Initialize the hand with a list of cards.
        :param cards: list of Card objects
        """
        self.hand = list(cards)  # All cards currently in hand
        self.activeCard = []  # Cards that have been drawn (active)
        self.amount = len(self.hand)  # Number of cards currently in hand

    def drawcard(self, index=0):
        """
        Draw one card from the hand at a given index.
        Moves the card from 'hand' to 'activeCard'. If no index is provided,
        draws the top (0) card. Returns None if the hand is empty or index is out of range.
        :param index: integer index in the hand list
        :return: Card object or None if hand is empty or index invalid
        """
        if not self.hand:
            return None  # No cards left to draw
        if index < 0 or index >= len(self.hand):
            return None
        card = self.hand.pop(index)
        self.activeCard.append(card)
        self.amount = len(self.hand)
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
    
    def return_cards(self):
        """
        Returns all active cards to the players hand. 
        I.E clears the activeCards list.
        """
        i, tmp = 0, len(self.activeCard)
        while i < tmp:
            self.hand.append(self.removeCard())
            i += 1
        self.amount = len(self.hand)

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

    def get_active_card(self):
        """
        Returns the list of active cards        
        """
        return self.activeCard
    
    def set_active_card(self, active_cards=[]):
        """
        Replace the active cards with a new list of active cards.

        :active_cards: List of card objects. Default param is an empty list.
        """
        self.activeCard = active_cards
        return self.activeCard
