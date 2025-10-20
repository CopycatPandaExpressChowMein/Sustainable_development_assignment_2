class Intelligence:
    """This is the AI logic And how it thinks"""

    def __init__(self, name="AI", hand=None):
        """
        Initializes the AI's hand and name.
        """
        self.setName(name)
        self.setHand(hand) 

    def setName(self, name):
        """Sets the name for the AI"""
        self.name = name

    def setHand(self, hand):
        """Sets the hand (cards) for the AI"""
        self.hand = hand

    def getHand(self):
        """Returns the AI's current hand"""
        return self.hand

    def getName(self):
        """Returns the name of the AI"""
        return self.name
