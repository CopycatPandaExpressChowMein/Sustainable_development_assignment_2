"""AI (Intelligence) module.

Contains the Intelligence class implementing selectable AI levels used in
single-player mode. Levels supported include 'top', 'random', and 'greedy'.
"""


class Intelligence:
    """AI logic with selectable intelligence levels.

    Levels supported:
    - 'random': chooses a random valid index from its hand
    - 'greedy': chooses the card with the highest value
    """

    def __init__(self, name="AI", hand=None, level="random"):
        """Initializes the AI's name, hand and intelligence level."""
        self.set_name(name)
        self.set_hand(hand)
        self.set_level(level)

    def set_name(self, name):
        """Set the AI name."""
        self.name = name

    def set_hand(self, hand):
        """Set the AI's CardHand."""
        self.hand = hand

    def get_hand(self):
        """Return the AI's current CardHand."""
        return self.hand

    def get_name(self):
        """Return the AI's name."""
        return self.name

    def set_level(self, level: str):
        """Set the intelligence level. Defaults to 'top' (play top card) if unknown.

        Supported levels: 'top', 'random', 'greedy'.
        """
        if level not in ("random", "greedy", "top"):
            level = "top"
        self.level = level

    def get_level(self) -> str:
        return getattr(self, "level", "random")

    def choose_index(self):
        """Choose an index from current hand according to intelligence level.

        Returns an integer index or None if no valid choice (e.g., empty hand).
        """
        hand = None
        try:
            hand = self.hand.getHand()
        except Exception:
            hand = None

        if not hand:
            return None

        if self.get_level() == "random":
            import random

            return random.randrange(0, len(hand))

        if self.get_level() == "top":
            return 0

        # greedy: choose the index of the highest-value card
        best_idx = 0
        best_val = -float("inf")
        for i, card in enumerate(hand):
            try:
                v = card.get_value()
            except Exception:
                v = 0
            if v > best_val:
                best_val = v
                best_idx = i
        return best_idx
