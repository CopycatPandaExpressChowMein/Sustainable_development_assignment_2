class Player:

    __name = ""
    __hand = object

    def __init__(self, name="Placeholder", hand=None):
        """ Initiates a player object, takes a String and CardHand parameter. 
            Uses default arguments in case no arguments are given."""
        self.set_name(name)
        self.set_hand(hand)

    def set_name(self, name):
        """Takes a String as a parameter and sets the private __name variable to that String."""
        if isinstance(name, str):
            self.__name = name
        else:
            print("Invalid argument, not a String or subclass of String.")

    def set_hand(self, hand):
        """Takes a CardHand object as a parameter and sets the private __card variable to that CardHand."""
        if type(hand, object):
            self.__hand = hand
        else:
            print("Invalid argument, not a CardHand object.")

    def get_name(self):
        """Returns the name of the player object as a String."""
        return self.__name 

    def get_hand(self):
        """Returns the CardHand of the player object."""
        return self.__hand

