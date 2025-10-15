class Player:
    """Object that retains info such as the name and CardHand of the  player.
    With the required methods to manipulate that information."""

    def __init__(self, name="Anonymous", hand=None):
        """Initializes a player object, takes a String and CardHand parameter.
        Uses the default arguments 'Placeholder' and 'None' in case no arguments are given for name and hand.
        """
        self.set_name(name)
        self.set_hand(hand)

    def __str__(self):
        print(f"Player: {self.__name} | Hand: {self.__hand}")

    def set_name(self, name):
        """Takes a String as an argument and sets the private __name variable to that argument.
        The String should be the name of the player."""
        self.__name = name
        return self.__name

    def set_hand(self, hand):
        """Takes a CardHand object as a parameter and sets the private __card variable to that CardHand.
        The CardHand should be the hand the player will use in a game."""
        self.__hand = hand
        return self.__hand

    def get_name(self):
        """Returns the name of the player object as a String."""
        return self.__name

    def get_hand(self):
        """Returns the CardHand of the player object."""
        return self.__hand
