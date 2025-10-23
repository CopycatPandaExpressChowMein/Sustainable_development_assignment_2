class Intelligence:
    """This is the AI logic And how it thinks"""

    def __init__(self, name="AI", hand=None):
        """
        Initializes the AI's hand and name.
        """
        self.set_name(name)
        self.set_hand(hand) 

    def set_name(self, name):
        """Sets the name for the AI"""
        self.name = name

    def set_hand(self, hand):
        """Sets the hand (cards) for the AI"""
        self.hand = hand

    def get_hand(self):
        """Returns the AI's current hand"""
        return self.hand

    def get_name(self):
        """Returns the name of the AI"""
        return self.name
    
