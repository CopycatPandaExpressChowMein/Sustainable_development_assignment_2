"""Card class representing a single playing card."""


class Card:
    def __init__(self, value, symbol, suit, color):
        """Initialize a card."""
        self.value = value
        self.symbol = symbol
        self.suit = suit
        self.color = color

    def __str__(self):
        return self.symbol
    
    # getter
    def get_value(self):
        return self.value

    def get_symbol(self):
        return self.symbol

    def get_suit(self):
        return self.suit

    def get_color(self):
        return self.color

    # setter
    def set_value(self, value):
        self.value = value

    def set_symbol(self, symbol):
        self.symbol = symbol

    def set_suit(self, suit):
        self.suit = suit

    def set_color(self, color):
        self.color = color

