"""Card module for representing a single playing card."""


class Card:
    """Represents a single playing card with a suit, symbol, value, and color."""

    def __init__(self, value, symbol, suit, color):
        """Initialize a Card object.

        :param value: Numeric value of the card (2–14)
        :param symbol: Unicode symbol for the card (e.g., 🂡)
        :param suit: The suit of the card (Spades, Hearts, Diamonds, Clubs)
        :param color: Color of the card (red or black)
        """
        self.value = value
        self.symbol = symbol
        self.suit = suit
        self.color = color

    def __str__(self):
        """Return the Unicode symbol when printing the card."""
        return self.symbol

    def get_value(self):
        """Return the numeric value of the card."""
        return self.value

    def get_symbol(self):
        """Return the Unicode symbol of the card."""
        return self.symbol

    def get_suit(self):
        """Return the suit of the card."""
        return self.suit

    def get_color(self):
        """Return the color of the card."""
        return self.color

    def set_value(self, value):
        """Set the card’s numeric value."""
        self.value = value

    def set_symbol(self, symbol):
        """Set the card’s Unicode symbol."""
        self.symbol = symbol

    def set_suit(self, suit):
        """Set the card’s suit."""
        self.suit = suit

    def set_color(self, color):
        """Set the card’s color."""
        self.color = color
