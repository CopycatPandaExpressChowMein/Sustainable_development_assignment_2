"""Core game module.

Contains the Game class which implements the main War game logic and state.
This module is intentionally free of direct long-running interactive loops so the
logic can be used programmatically by tests and by the Shell CLI.
"""

import datetime

try:  # Try imports for executing Main normally
    from Deck import Deck
    from Player import Player
    from Intelligence import Intelligence
    from CardHand import CardHand
    from Highscore import Highscore
except:  # Except imports for UnitTesting. To prevent module not found Error.
    from .Deck import Deck
    from .Player import Player
    from .Intelligence import Intelligence
    from .CardHand import CardHand
    from .Highscore import Highscore


class Game:
    """Represents the game logic and contains the methods to run and manipulate the game."""

    def __init__(self):
        """Initialize the Game with default values."""
        self.__highscore = Highscore()
        self.__active_game = False

    def start(self, mode=1, player1="Anonymous", player2="Anonymous", ai_level="top"):
        """Start a new game and deal cards to players.

        :param mode: 1 for singleplayer or 2 for two-player
        :param player1: name of player 1 (default 'Anonymous')
        :param player2: name of player 2 (ignored in singleplayer)
        :param ai_level: intelligence level for AI players ('top', 'random', 'greedy')
        """
        self.__player1 = Player(player1)
        # Checks whether the current mode is single or multiplayer and assigns player2 accordingly.
        self.__player2 = (
            Player(player2) if mode == 2 else Intelligence("AI", level=ai_level)
        )
        self.__players = [self.__player1, self.__player2]

        self.__deck = Deck()
        hands = self.__deck.split()
        self.__players[0].set_hand(CardHand(hands[0]))
        self.__players[1].set_hand(CardHand(hands[1]))

        for player in self.__players:
            self.__highscore.add_player(player.get_name())

        self.num_draws = 0  # Counter for the number of draws taken per game. Incremented each time cards are drawn.

        self.__active_game = True

    def get_active_game(self):
        """Return True when a game is currently active, otherwise False."""
        return self.__active_game

    def cheat(self):
        """Sets the value of all of Player1s cards to 99"""
        print("Shhh. Be sneaky... All your cards now have a value of 99.")
        player1_deck = self.__players[0].get_hand().get_hand()
        for card in player1_deck:
            card.set_value(99)

    def _pause(self):
        """Pause helper that avoids blocking when running tests."""
        try:
            import sys

            # If unittest is running, skip pause to avoid blocking automated tests
            if "unittest" in sys.modules:
                return
        except Exception:
            pass
        try:
            input("Press to continue...")
        except Exception:
            return

    # TODO Graphics
    def draw_cards(self, internal=False):
        """Execute a single draw round and resolve the result.

        When ``internal`` is True the call is part of recursive war resolution
        and will not increment the public draw counter.
        """

        player1_hand = self.__players[0].get_hand()
        player2_hand = self.__players[1].get_hand()

        player1_name = self.__players[0].get_name()
        player2_name = self.__players[1].get_name()

        # Check if any player ran out of cards, game over condition
        if len(player1_hand.get_hand()) == 0:
            # Player 2 wins, player 1 ran out of cards
            self.__highscore.add_statistics(
                player2_name, True, self.num_draws, datetime.date.today()
            )

            p2_win_msg = f""" 

                    ██╗    ██╗██╗███╗   ██╗
                    ██║    ██║██║████╗  ██║
                    ██║ █╗ ██║██║██╔██╗ ██║
                    ██║███╗██║██║██║╚██╗██║
                    ╚███╔███╔╝██║██║ ╚████║
                    ╚══╝╚══╝ ╚═╝╚═╝  ╚═══╝
                    {player2_name + " won the game!"}
                    {player1_name + " loses...."}
                Enter 'start' to begin another game!
                            """
            print(p2_win_msg)
            return
        elif len(player2_hand.get_hand()) == 0:
            # Player 1 wins, player 2 ran out of cards
            self.__highscore.add_statistics(
                player1_name, True, self.num_draws, datetime.date.today()
            )

            p1_win_msg = f"""

                    ██╗    ██╗██╗███╗   ██╗
                    ██║    ██║██║████╗  ██║
                    ██║ █╗ ██║██║██╔██╗ ██║
                    ██║███╗██║██║██║╚██╗██║
                    ╚███╔███╔╝██║██║ ╚████║
                    ╚══╝╚══╝ ╚═╝╚═╝  ╚═══╝
                    {player1_name + " won the game!"}
                    {player2_name + " loses...."}
                Enter 'start' to begin another game!
                            """
            print(p1_win_msg)
            return

        screen1 = f"""
        {player2_name:^50}
        ▐▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▌
        ▐                                                ▌
        ▐         {player2_hand.get_amount():<2}🂠                                    ▌
        ▐                                                ▌
        ▐                                                ▌
        ▐                                                ▌
        ▐                      Draw!                     ▌
        ▐                                                ▌
        ▐                                                ▌
        ▐                                                ▌
        ▐                                    🂠{player1_hand.get_amount():>2}         ▌
        ▐                                                ▌
        ▐▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▌
        {player1_name:^50}
                    """
        print(screen1)
        self._pause()

        # Each player draws a card. If a player provides a choose_index method (AI), use it.
        idx1 = None
        idx2 = None
        try:
            if hasattr(self.__players[0], "choose_index"):
                idx1 = self.__players[0].choose_index()
        except Exception:
            idx1 = None
        try:
            if hasattr(self.__players[1], "choose_index"):
                idx2 = self.__players[1].choose_index()
        except Exception:
            idx2 = None

        player1_card = (
            player1_hand.draw_card(idx1)
            if idx1 is not None
            else player1_hand.draw_card()
        )
        player2_card = (
            player2_hand.draw_card(idx2)
            if idx2 is not None
            else player2_hand.draw_card()
        )
        # Only count the draw for top-level (external) invocations. Internal recursive
        # draws during war resolution should not increment the public draw counter.
        if not internal:
            self.num_draws += 1

        screen2 = f"""
        {player2_name:^50}
        ▐▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▌
        ▐                       ?                        ▌
        ▐         {player2_hand.get_amount():<2}🂠           🂠                        ▌
        ▐                                                ▌
        ▐                                                ▌
        ▐                                                ▌
        ▐                    Reveal...                   ▌
        ▐                                                ▌
        ▐                                                ▌
        ▐                                                ▌
        ▐                       🂠           🂠{player1_hand.get_amount():>2}          ▌
        ▐                       ?                        ▌
        ▐▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▌
        {player1_name:^50}
                    """
        print(screen2)
        self._pause()

        # Compare card values using correct get_value() method
        if player1_card.get_value() > player2_card.get_value():
            player2_active_cards = player2_hand.get_active_card()
            save_len = len(player2_active_cards)
            i, tmp = 0, len(player2_active_cards)
            while i < tmp:
                player1_hand.add_card(player2_hand.remove_card())
                i += 1
            player1_hand.return_cards()

            screen3alt1 = f"""
        {player2_name:^50}
        ▐▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▌
        ▐                       {player2_card.get_value():<2}                       ▌
        ▐         {player2_hand.get_amount():<2}🂠           {player2_card.get_symbol()}                        ▌
        ▐                                                ▌
        ▐                                                ▌
        ▐                                                ▌
        ▐{(player1_name + " wins! They get " + str(save_len) + " card(s)"):^48}▌
        ▐                                                ▌
        ▐                                                ▌
        ▐                                                ▌
        ▐                       {player1_card.get_symbol()}           🂠{player1_hand.get_amount():>2}          ▌
        ▐                       {player1_card.get_value():<2}                       ▌
        ▐▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▌
        {player1_name:^50}
                        """
            print(screen3alt1)

        elif player1_card.get_value() < player2_card.get_value():
            player1_active_cards = player1_hand.get_active_card()
            save_len = len(player1_active_cards)
            i, tmp = 0, len(player1_active_cards)
            while i < tmp:
                player2_hand.add_card(player1_hand.remove_card())
                i += 1
            player2_hand.return_cards()

            screen3alt2 = f"""
        {player2_name:^50}
        ▐▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▌
        ▐                       {player2_card.get_value():<2}                       ▌
        ▐         {player2_hand.get_amount():<2}🂠           {player2_card.get_symbol()}                        ▌
        ▐                                                ▌
        ▐                                                ▌
        ▐                                                ▌
        ▐{(player2_name + " wins! They get " + str(save_len) + " card(s)"):^48}▌
        ▐                                                ▌
        ▐                                                ▌
        ▐                                                ▌
        ▐                       {player1_card.get_symbol()}           🂠{player1_hand.get_amount():>2}          ▌
        ▐                       {player1_card.get_value():<2}                       ▌
        ▐▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▌
        {player1_name:^50}
                        """
            print(screen3alt2)

        else:
            screen3alt3 = f"""
        {player2_name:^50}
        ▐▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▌
        ▐                       {player2_card.get_value():<2}                       ▌
        ▐         {player2_hand.get_amount():<2}🂠           {player2_card.get_symbol()}                        ▌
        ▐                                                ▌
        ▐                                                ▌
        ▐                                                ▌
        ▐                      War!                      ▌
        ▐                                                ▌
        ▐                                                ▌
        ▐                                                ▌
        ▐                       {player1_card.get_symbol()}           🂠{player1_hand.get_amount():>2}          ▌
        ▐                       {player1_card.get_value():<2}                       ▌
        ▐▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▌
        {player1_name:^50}
                        """
            print(screen3alt3)
            self._pause()

            # Check if players have enough cards for war
            if len(player1_hand.get_hand()) < 2:  # Player 1 doesn't have enough
                for card in player1_hand.get_active_card():
                    player2_hand.add_card(player1_hand.remove_card())
                player2_hand.return_cards()

                screen3alt3 = f"""
        {player2_name:^50}
        ▐▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▌
        ▐                       {player2_card.get_value():<2}                       ▌
        ▐         {player2_hand.get_amount():<2}🂠           {player2_card.get_symbol()}                        ▌
        ▐                                                ▌
        ▐                                                ▌
        ▐                                                ▌
        ▐{(player1_name + " doesn't have enough cards!"):^48}▌
        ▐                                                ▌
        ▐                                                ▌
        ▐                                                ▌
        ▐                       {player1_card.get_symbol()}           🂠{player1_hand.get_amount():>2}          ▌
        ▐                       {player1_card.get_value():<2}                       ▌
        ▐▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▌
        {player1_name:^50}
                        """
                print(screen3alt3)

                return
            elif len(player2_hand.get_hand()) < 2:  # Player 2 doesn't have enough cards
                for card in player2_hand.get_active_card():
                    player1_hand.add_card(player2_hand.remove_card())
                player1_hand.return_cards()

                screen3alt3 = f"""
        {player2_name:^50}
        ▐▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▌
        ▐                       {player2_card.get_value():<2}                       ▌
        ▐         {player2_hand.get_amount():<2}🂠           {player2_card.get_symbol()}                        ▌
        ▐                                                ▌
        ▐                                                ▌
        ▐                                                ▌
        ▐{(player2_name + " doesn't have enough cards!"):^48}▌
        ▐                                                ▌
        ▐                                                ▌
        ▐                                                ▌
        ▐                       {player1_card.get_symbol()}           🂠{player1_hand.get_amount():>2}          ▌
        ▐                       {player1_card.get_value():<2}                       ▌
        ▐▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▌
        {player1_name:^50}
                        """
                print(screen3alt3)

                return

            # Each player places one card face down (internal mechanics, do not
            # increment the public draw counter)
            player1_hand.draw_card()
            player2_hand.draw_card()

            screen2 = f"""
        {player2_name:^50}
        ▐▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▌
        ▐                       ?                        ▌
        ▐         {player2_hand.get_amount():<2}🂠           🂠                        ▌
        ▐                                                ▌
        ▐                                                ▌
        ▐                                                ▌
        ▐             Place cards face down...           ▌
        ▐                                                ▌
        ▐                                                ▌
        ▐                                                ▌
        ▐                       🂠           🂠{player1_hand.get_amount():>2}          ▌
        ▐                       ?                        ▌
        ▐▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▌
        {player1_name:^50}
                    """
            print(screen2)
            self._pause()

            # Recursively call draw_cards to determine who wins the war. Mark
            # this as internal so the public draw counter isn't incremented again.
            self.draw_cards(internal=True)

    def name_change(self, current_name, new_name):
        """Change a player's name and persist the updated highscores.

        This updates the player's key in the Highscore object and triggers
        a save to the configured highscores file.

        Parameters
        ----------
        current_name : str
            The existing player name to replace.
        new_name : str
            The new player name.
        """
        self.__highscore.update_player_name(current_name, new_name)
        self.save_highscore()

    # Functions for manipulating highscores
    def show_highscore(self):
        """Prints the current values of the highscore object as a String."""
        print(self.__highscore)

    def save_highscore(self):
        """Saves the current values of the highscore object."""
        self.__highscore.save_highscores()
