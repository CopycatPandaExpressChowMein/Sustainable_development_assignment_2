import datetime
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

        self.num_draws = 0 #Counter for the number of draws taken per game. Incremented each time cards are drawn.

        self.__active_game = True
        

    def get_active_game(self):
        """Returns a bool indicating whether or not a game is ongoing or not."""
        return self.__active_game

    def cheat(self):
        """Allows you to cheat in the game"""
        pass

    #TODO Graphics
    def draw_cards(self):

        player1_hand = self.__players[0].get_hand()
        player2_hand = self.__players[1].get_hand()

        player1_name = self.__players[0].get_name()
        player2_name = self.__players[1].get_name()

        # Check if any player ran out of cards, game over condition
        if len(player1_hand.getHand()) == 0:
            #Player 2 wins, player 1 ran out of cards
            print(f"{player2_name} wins the game! {player1_name} has no more cards.")
            self.__highscore.add_statistics(player2_name, True, self.num_draws, datetime.date.today())
            return
        elif len(player2_hand.getHand()) == 0:
            #Player 1 wins, player 2 ran out of cards
            print(f"{player1_name} wins the game! {player2_name} has no more cards.")
            self.__highscore.add_statistics(player1_name, True, self.num_draws, datetime.date.today())
            return

        # Each player draws a card
        player1_card = player1_hand.drawcard()
        player2_card = player2_hand.drawcard()
        self.num_draws += 1


        # Compare card values using correct get_value() method
        if player1_card.get_value() > player2_card.get_value():
            player2_active_cards = player2_hand.get_active_card()
            print(f"{player1_name} wins the round and takes {len(player2_active_cards)} cards from {player2_name}.")
            i, tmp = 0, len(player2_active_cards)
            while i < tmp:
                player1_hand.addCard(player2_hand.removeCard())
                i += 1
            player1_hand.return_cards()
        elif player1_card.get_value() < player2_card.get_value():
            player1_active_cards = player1_hand.get_active_card()
            print(f"{player2_name} wins the round and takes {len(player1_active_cards)} cards from {player1_name}.")
            i, tmp = 0, len(player1_active_cards)
            while i < tmp:
                player2_hand.addCard(player1_hand.removeCard())
                i += 1
            player2_hand.return_cards()
        else:
            print("War! Players place one card face down and one card face up.")
            # Check if players have enough cards for war
            if len(player1_hand.getHand()) < 2:
                print(f"{player1_name} cannot continue war - loses!")
                for card in player1_hand.get_active_card():
                    player2_hand.addCard(player1_hand.removeCard())
                player2_hand.return_cards()
                return
            if len(player2_hand.getHand()) < 2:
                print(f"{player2_name} cannot continue war - loses!")
                for card in player2_hand.get_active_card():
                    player1_hand.addCard(player2_hand.removeCard())
                player1_hand.return_cards()
                return

            # Each player places one card face down (on war pile)
            player1_hand.drawcard()
            player2_hand.drawcard()
            self.num_draws += 1


            # Recursively call draw_cards to determine who wins the war
            self.draw_cards()


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

