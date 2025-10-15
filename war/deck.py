"""Deck class using Unicode playing card symbols (U+1F0A0–U+1F0FF)."""

import random
from .Card import Card

class Deck:
    """Represents a standard deck of 52 Unicode playing cards."""

    def __init__(self):
        """Create and shuffle the Unicode card deck."""
        self._deck = self.create()
        self.shuffle()

    def create(self):
        """Create a deck of cards using Unicode playing card characters."""
        suits = ["Spades", "Hearts", "Diamonds", "Clubs"]
        colors = ["black", "red", "red", "black"]

        unicode_cards = [
            # Spades
            "🂡","🂢","🂣","🂤","🂥","🂦","🂧","🂨","🂩","🂪","🂫","🂭","🂮",
            # Hearts
            "🂱","🂲","🂳","🂴","🂵","🂶","🂷","🂸","🂹","🂺","🂻","🂽","🂾",
            # Diamonds
            "🃁","🃂","🃃","🃄","🃅","🃆","🃇","🃈","🃉","🃊","🃋","🃍","🃎",
            # Clubs
            "🃑","🃒","🃓","🃔","🃕","🃖","🃗","🃘","🃙","🃚","🃛","🃝","🃞"
        ]

        cards = []
        idx = 0
        for s_index, suit in enumerate(suits):
            color = colors[s_index]
            for value in range(2, 15):
                symbol = unicode_cards[idx]
                idx = idx + 1
                cards.append(Card(value, symbol, suit, color))
        return cards

    def shuffle(self):
        """Shuffle the deck."""
        random.shuffle(self._deck)

    def split(self):
        """Split the deck evenly for two players."""
        half = len(self._deck) // 2
        return self._deck[:half], self._deck[half:]

    def getDeck(self):
        """Return the full deck of cards."""
        return self._deck

    def setDeck(self, deck):
        """Replace the current deck with a new list of cards."""
        self._deck = deck



