from Deck import Deck
from Player import Player
from Intelligence import Intelligence
from CardHand import CardHand
from Highscore import Highscore



class Game:
    """Represents the game logic and contains the methods to run and manipulate the game."""

    
    def __init__(self):
        """initialises the game with default value"""
        self.__highscore = Highscore()
        self.__active_game = False

    def start(self,  mode=1, player1="Anonymous", player2="Anonymous"):
        """
        Starts the game.
        
        :player1: Name of player 1 as a String. Default param is Anonymous.
        :player2: Name of player 2 as a String. Default param is Anonymous.
        :mode: The gamemode as an int, 1 representing singleplayer and 2 multiplayer. Default param is 1 (Singleplayer)
        """
        self.__player1 = Player(player1)
        self.__player2 = Player(player2) if mode == 2 else Intelligence("AI") #Checks whether the current mode is single or multiplayer and assigns player2 accordingly.
        self.__players = [self.__player1, self.__player2]
        
        self.__deck = Deck()
        hands = self.__deck.split()
        self.__players[0].set_hand(CardHand(hands[0]))
        self.__players[1].set_hand(CardHand(hands[1]))

        for player in self.__players:
            self.__highscore.add_player(player.get_name())

        print(f"{self.__player1.get_name()} vs {self.__player2.get_name()}, The Game has started!")
        self.__active_game = True

    def get_active_game(self):
        """Returns a bool indicating whether or not a game is ongoing or not."""
        return self.__active_game


    #TODO
    def cheat(self):
        """allows you to cheat in the game"""
        print("Place holder cheat")

    #TODO
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

    def name_change(self, current_name, new_name):
        """ 
        Takes a current and new name and updates it in the highscore object.
        Prints the change to cmd.
        And then saves the highscore object to json.
        """
        self.__highscore.update_player_name(current_name, new_name)
        self.save_highscore()


    #Functions for manipulating highscores
    def show_highscore(self):
        """Prints the current values of the highscore object as a String."""
        print(self.__highscore)

    def save_highscore(self):
        """Saves the current values of the highscore object."""
        self.__highscore.save_highscores()

