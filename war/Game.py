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
        ai = Intelligence("AI")
        self.players = [human, ai]
        self.deck.create()
        self.deck.shuffle()
        hands = self.deck.split()
        self.players[0].set_hand(CardHand(hands[0]))
        self.players[1].set_hand(CardHand(hands[1]))

        print(f"{human.get_name()} vs AI, The Game has started!")

    def pickmode(self):
        """allows player to pick a mode"""
        self.mode = "You against AI"
        print("Standard War card game")

    def cheat(self):
        """allows you to cheat in the game"""
        print("Reveals cards in hand:")
        for player in self.players:
            hand = player.get_hand()
            print(
                f"{player.get_name()} hand: {[card.get_value() for card in hand.getHand()]}"
            )

    def draw_cards(self, war_pile=None):
        # Initialize war pile to keep cards on table for war rounds
        if war_pile is None:
            war_pile = []

        hand0 = self.players[0].get_hand()
        hand1 = self.players[1].get_hand()

        # Check if any player ran out of cards, game over condition
        if len(hand0.getHand()) == 0:
            print(f"{self.players[1].get_name()} wins the game! {self.players[0].get_name()} has no more cards.")
            return
        if len(hand1.getHand()) == 0:
            print(f"{self.players[0].get_name()} wins the game! {self.players[1].get_name()} has no more cards.")
            return

        # Each player draws a card
        card1 = hand0.drawcard()
        card2 = hand1.drawcard()

        print(f"{self.players[0].get_name()} played {card1}")
        print(f"{self.players[1].get_name()} played {card2}")

        # Put these cards on war pile
        war_pile.extend([card1, card2])

        # Compare card values using correct get_value() method
        if card1.get_value() > card2.get_value():
            print(f"{self.players[0].get_name()} wins the round and takes {len(war_pile)} cards.")
            # Fix: add each card using addCard instead of addcards
            for c in war_pile:
                hand0.addCard(c)
            war_pile.clear()
        elif card1.get_value() < card2.get_value():
            print(f"{self.players[1].get_name()} wins the round and takes {len(war_pile)} cards.")
            for c in war_pile:
                hand1.addCard(c)
            war_pile.clear()
        else:
            print("War! Players place one card face down and one card face up.")

            # Check if players have enough cards for war
            if len(hand0.getHand()) < 2:
                print(f"{self.players[0].get_name()} cannot continue war - loses!")
                for c in war_pile + hand0.getHand():
                    hand1.addCard(c)
                hand0.getHand().clear()
                return
            if len(hand1.getHand()) < 2:
                print(f"{self.players[1].get_name()} cannot continue war - loses!")
                for c in war_pile + hand1.getHand():
                    hand0.addCard(c)
                hand1.getHand().clear()
                return

            # Each player places one card face down (on war pile)
            war_pile.append(hand0.drawcard())
            war_pile.append(hand1.drawcard())

            # Recursively call draw_cards to determine who wins the war
            self.draw_cards(war_pile)

