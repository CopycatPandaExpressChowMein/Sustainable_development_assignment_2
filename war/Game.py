from Deck import Deck
from Player import Player
from Intelligence import Intelligence
from CardHand import CardHand


class Game:
    """Represent the game logic and also the state of the game"""

    def __init__(self):
        """initialises the game with default value"""
        self.mode = "You against AI"
        self.deck = Deck()
        self.players = []

    def start(self):
        """Starts the game"""
        player_name = input("Enter your name:")
        human = Player(player_name)
        ai = Intelligance("AI")  # AI opponent, must support CardHand interface
        self.players = [human, ai]
        self.deck.create()
        self.deck.shuffle()
        hands = self.deck.split()  # Assumes split returns two lists of Card objects
        self.players[0].setHand(CardHand(hands[0]))
        self.players[1].setHand(CardHand(hands[1]))
        print(f"{human.getName()} vs AI, The Game has started!")

    def pickmode(self):
        """allows player to pick a mode"""
        self.mode = "You against AI"
        print("Standard War card game")

    def cheat(self):
        """allows you to cheat in the game"""
        print("Reveals cards in hand:")
        for player in self.players:
            hand = player.getHand()
            print(
                f"{player.getName()} hand: {[card.getValue() for card in hand.getHand()]}"
            )
