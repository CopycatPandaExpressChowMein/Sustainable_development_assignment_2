import datetime
try: #Try imports for executing Main normally
    from Deck import Deck
    from Player import Player
    from Intelligence import Intelligence
    from CardHand import CardHand
    from Highscore import Highscore
except: #Except imports for UnitTesting. To prevent module not found Error.
    from .Deck import Deck
    from .Player import Player
    from .Intelligence import Intelligence
    from .CardHand import CardHand
    from .Highscore import Highscore



class Game:
    """Represents the game logic and contains the methods to run and manipulate the game."""

    
    def __init__(self):
        """initialises the game with default value"""
        self.__highscore = Highscore()
        self.__active_game = False

    def start(self,  mode=1, player1="Anonymous", player2="Anonymous", ai_level="top"):
        """
        Starts the game.
        
        :player1: Name of player 1 as a String. Default param is Anonymous.
        :player2: Name of player 2 as a String. Default param is Anonymous.
        :mode: The gamemode as an int, 1 representing singleplayer and 2 multiplayer. Default param is 1 (Singleplayer)
        """
        self.__player1 = Player(player1)
        # Checks whether the current mode is single or multiplayer and assigns player2 accordingly.
        self.__player2 = Player(player2) if mode == 2 else Intelligence("AI", level=ai_level)
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
<<<<<<< HEAD
        """Allows you to cheat in the game"""
        # Interactive wrapper - kept for compatibility. No-op by default.
        return None

    def cheat_swap(self, from_name: str, to_name: str, index_from: int = 0, index_to: int = 0) -> bool:
        """Programmatic cheat: swap a card from one player's hand to another player's hand.

        Finds players by name in the current game and swaps the card at index_from in
        from_name's hand with the card at index_to in to_name's hand.

        Returns True on successful swap, False if players not found or indices invalid.
        This method performs pure game-state changes and does not interact with I/O.
        """
        # Locate players
        players = getattr(self, "_Game__players", None)
        if not players:
            return False

        p_from = None
        p_to = None
        for p in players:
            try:
                if p.get_name() == from_name:
                    p_from = p
                if p.get_name() == to_name:
                    p_to = p
            except Exception:
                continue

        if p_from is None or p_to is None:
            return False

        hand_from = p_from.get_hand().getHand()
        hand_to = p_to.get_hand().getHand()

        # Validate indices
        if index_from < 0 or index_from >= len(hand_from):
            return False
        if index_to < 0 or index_to >= len(hand_to):
            return False

        # Perform swap
        card_from = hand_from.pop(index_from)
        card_to = hand_to.pop(index_to)

        # insert swapped cards back at the requested positions
        hand_from.insert(index_from, card_to)
        hand_to.insert(index_to, card_from)

        # Update amount fields on CardHand
        try:
            p_from.get_hand().amount = len(hand_from)
            p_to.get_hand().amount = len(hand_to)
        except Exception:
            pass

        return True
=======
        """Display both players' hands and allow swapping one card.

        This helper is intended for testing. It shows each player's hand and
        lets the user swap a single card between the selected player and the
        opponent. Swapped-in cards are placed on top of each hand so they will
        be drawn next.
        """
        # Ensure players are initialized
        if not getattr(self, "players", None) or len(self.players) < 2:
            print("No active game or fewer than two players. Start a game first to use cheat().")
            return

        # Use the game's players list
        players = self.players

        # Display each player's hand with indices
        for i, p in enumerate(players):
            hand = p.get_hand()
            cards = hand.getHand() if hand is not None else []
            display = ", ".join(f"[{idx}] {str(c)}" for idx, c in enumerate(cards))
            print(f"{i+1}) {p.get_name()} - {len(cards)} cards: {display}")

        # Prompt for which player to act as (index or name)
        choice = input("Which player are you? Enter 1 or 2 (or player name): ").strip()
        src_idx = None
        if choice in ("1", "2"):
            src_idx = int(choice) - 1
        else:
            # Match by name
            for i, p in enumerate(players):
                if p.get_name() == choice:
                    src_idx = i
                    break

        if src_idx is None or src_idx not in (0, 1):
            print("Invalid player selection. Aborting cheat.")
            return

        tgt_idx = 1 - src_idx
        src_hand_obj = players[src_idx].get_hand()
        tgt_hand_obj = players[tgt_idx].get_hand()

        if src_hand_obj is None or tgt_hand_obj is None:
            print("One of the players does not have a hand. Aborting cheat.")
            return

        src_hand = src_hand_obj.getHand()
        tgt_hand = tgt_hand_obj.getHand()

        if not src_hand:
            print(f"{players[src_idx].get_name()} has no cards to swap.")
            return
        if not tgt_hand:
            print(f"{players[tgt_idx].get_name()} has no cards to swap.")
            return

        # Show detailed hands
        print(f"\nYour hand ({players[src_idx].get_name()}):")
        for i, c in enumerate(src_hand):
            print(f"  {i}: {c}")
        print(f"\nOpponent's hand ({players[tgt_idx].get_name()}):")
        for i, c in enumerate(tgt_hand):
            print(f"  {i}: {c}")

        try:
            s_index = int(input("Enter index of your card to give away: ").strip())
            t_index = int(input("Enter index of opponent's card to take: ").strip())
        except ValueError:
            print("Invalid index input. Aborting cheat.")
            return

        if s_index < 0 or s_index >= len(src_hand) or t_index < 0 or t_index >= len(tgt_hand):
            print("Index out of range. Aborting cheat.")
            return

        # Swap the selected cards and place the taken cards on top
        s_card = src_hand.pop(s_index)
        t_card = tgt_hand.pop(t_index)

        src_hand.insert(0, t_card)
        tgt_hand.insert(0, s_card)

        print(f"Swapped your {s_card} with opponent's {t_card}. The taken cards were placed on top of each hand.")
>>>>>>> 831cad314fb4580bade8ae3334a46a5903dadd41

    #TODO Graphics
    def draw_cards(self):

        

        player1_hand = self.__players[0].get_hand()
        player2_hand = self.__players[1].get_hand()

        player1_name = self.__players[0].get_name()
        player2_name = self.__players[1].get_name()
    


        # Check if any player ran out of cards, game over condition
        if len(player1_hand.getHand()) == 0:
            #Player 2 wins, player 1 ran out of cards
            self.__highscore.add_statistics(player2_name, True, self.num_draws, datetime.date.today())

            p2_win_msg =    f""" 

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
        elif len(player2_hand.getHand()) == 0:
            #Player 1 wins, player 2 ran out of cards
            self.__highscore.add_statistics(player1_name, True, self.num_draws, datetime.date.today())

            p1_win_msg =    f"""

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
        

        screen1 =   f"""
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
        input("Press to continue...")

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

        player1_card = player1_hand.drawcard(idx1) if idx1 is not None else player1_hand.drawcard()
        player2_card = player2_hand.drawcard(idx2) if idx2 is not None else player2_hand.drawcard()
        self.num_draws += 1

        screen2 =   f"""
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
        input("Press to continue...")

        # Compare card values using correct get_value() method
        if player1_card.get_value() > player2_card.get_value():
            player2_active_cards = player2_hand.get_active_card()
            save_len = len(player2_active_cards)
            i, tmp = 0, len(player2_active_cards)
            while i < tmp:
                player1_hand.addCard(player2_hand.removeCard())
                i += 1
            player1_hand.return_cards()

            screen3alt1 =   f"""
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
                player2_hand.addCard(player1_hand.removeCard())
                i += 1
            player2_hand.return_cards()

            screen3alt2 =   f"""
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
            screen3alt3 =   f"""
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
            input("Press to continue...")

            # Check if players have enough cards for war
            if len(player1_hand.getHand()) < 2: #Player 1 doesn't have enough
                for card in player1_hand.get_active_card():
                    player2_hand.addCard(player1_hand.removeCard())
                player2_hand.return_cards()

                screen3alt3 =   f"""
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
            elif len(player2_hand.getHand()) < 2: #Player 2 doesn't have enough cards
                for card in player2_hand.get_active_card():
                    player1_hand.addCard(player2_hand.removeCard())
                player1_hand.return_cards()

                screen3alt3 =   f"""
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



            # Each player places one card face down
            player1_hand.drawcard()
            player2_hand.drawcard()
            self.num_draws += 1

            screen2 =   f"""
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
            input("Press to continue...")

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

