class Intelligence:
    """This is the AI logic And how it thinks"""

    def __init__(self, name="AI"):
        """
        Initializes the AI's hand and name.
        """
        self.name = name
        self.hand = None  # The cards AI holds

    def setHand(self, hand):
        """Sets the hand (cards) for the AI"""
        self.hand = hand

    def getHand(self):
        """Returns the AI's current hand"""
        return self.hand

    def getName(self):
        """Returns the name of the AI"""
        return self.name
