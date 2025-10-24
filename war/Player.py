"""Player model module.

Defines the Player class which holds a player's name and CardHand. This
lightweight model is used by Game and by tests and intentionally keeps I/O
out of the data model.
"""


class Player:
    """
    Object that retains info such as the name and CardHand of the  player.
    With the required methods to manipulate that information.
    """

    def __init__(self, name="Anonymous", hand=None):
        """
        Initializes a player object with a name and CardHand.

        :name: The name of the player as a String. Default param is Anonymous.
        :hand: The hand of cards the player has as a CardHand object. Default param is None.
        """
        self.set_name(name)
        self.set_hand(hand)

    def __str__(self):
        """
        Defines how to represent the player as a String.
        Prints the name of the player, followed by their given CardHand.
        """
        return(f"Player: {self.__name} | Hand: {self.__hand}")
    
    def set_name(self, name):
        """
        Sets the name variable to the given argument.
        
        :name: The name of the player as a String.
        """
        self.__name = name
        return self.__name

    def set_hand(self, hand):
        """
        Sets the card variable to the given argument.
        
        :hand: The hand of cards the player has as a CardHand object.
        """
        self.__hand = hand
        return self.__hand

    def get_name(self):
        """
        Returns the name of the player object as a String.
        """
        return self.__name

    def get_hand(self):
        """
        Returns the CardHand of the player object.
        """
        return self.__hand
