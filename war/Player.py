"""Player model module.

Defines the Player class which holds a player's name and CardHand. This
lightweight model is used by Game and by tests and intentionally keeps I/O
out of the data model.
"""


class Player:
    """Lightweight player model storing name and CardHand.

    This class is intentionally small and keeps I/O out of the model so
    it can be used easily by the Game logic and unit tests.
    """

    def __init__(self, name="Anonymous", hand=None):
        """Initialize a Player with an optional CardHand.

        :param name: player name (default 'Anonymous')
        :param hand: CardHand instance or None
        """
        self.set_name(name)
        self.set_hand(hand)

    def __str__(self):
        """Return a concise string representation of the Player."""
        return f"Player: {self.__name} | Hand: {self.__hand}"

    def set_name(self, name):
        """Set the player's name and return it.

        :param name: new player name
        :return: the stored name
        """
        self.__name = name
        return self.__name

    def set_hand(self, hand):
        """Set the player's CardHand and return it.

        :param hand: CardHand instance or None
        :return: the stored CardHand
        """
        self.__hand = hand
        return self.__hand

    def get_name(self):
        """Return the player's name as a string."""
        return self.__name

    def get_hand(self):
        """Return the player's CardHand (may be None)."""
        return self.__hand
