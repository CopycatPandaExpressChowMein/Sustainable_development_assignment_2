"""CardHand class for managing a player's hand of cards."""

class CardHand:
    def __init__(self, cards=None):
        """Initialize the CardHand.

        Create a new CardHand optionally populated with a list of Card objects.

        :param cards: list of Card objects or None
        """
        if cards is None:
            cards = []
        self.hand = list(cards)  # All cards currently in hand
        self.activeCard = []  # Cards that have been drawn (active)
        self.amount = len(self.hand)  # Number of cards currently in hand

    def drawcard(self, index=0):
        """Draw a card from the hand at the given index.

        Moves the card from `hand` to `activeCard`. If no index is provided,
        draws the top (0) card. Returns None if the hand is empty or index
        is invalid.
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
        """Add a Card object to the hand.

        :param card: Card object to append
        """
        self.hand.append(card)  # Add the card to the hand
        self.amount = len(self.hand)  # Update the count

    def removeCard(self):
        """Remove and return one active card.

        Returns the earliest active card or None if there are no active cards.
        """
        if not self.activeCard:
            return None
        return self.activeCard.pop(0)  # Remove and return one active card
    
    def return_cards(self):
        """Return all active cards back into the player's hand.

        Clears the active cards list by moving them back into `hand`.
        """
        i, tmp = 0, len(self.activeCard)
        while i < tmp:
            self.hand.append(self.removeCard())
            i += 1
        self.amount = len(self.hand)

    def getHand(self):
        """Return the current list of Card objects in the hand."""
        return self.hand

    def setHand(self, hand):
        """Replace the hand with a new list of cards.

        :param hand: list of Card objects
        """
        self.hand = list(hand)  # Set a new hand
        self.amount = len(hand)  # Update the count

    def get_active_card(self):
        """Return the list of active cards."""
        return self.activeCard
    
    def set_active_card(self, active_cards=[]):
        """Replace the active cards with a new list.

        :param active_cards: list of Card objects
        """
        self.activeCard = list(active_cards)
        return self.activeCard
    
    def get_amount(self):
        return self.amount

    def set_amount(self, amount):
        self.amount = amount
        return self.amount
    
