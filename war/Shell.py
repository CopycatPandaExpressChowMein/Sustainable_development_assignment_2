import cmd
try: #Try imports for executing Main normally
    from Game import Game
except: #Except imports for UnitTesting. To prevent module not found Error.
    from .Game import Game

#TODO Rework cheat to be more aligned with requirements, "cheat that one can use for testing purposes and reach the end of the game faster"
#TODO Rework Graphical interface

class Shell(cmd.Cmd):
    """handles the interface of the game, input and output."""
    intro = """ 
    
                ██╗    ██╗ █████╗ ██████╗ ██╗
                ██║    ██║██╔══██╗██╔══██╗██║
                ██║ █╗ ██║███████║██████╔╝██║
                ██║███╗██║██╔══██║██╔══██╗╚═╝
                ╚███╔███╔╝██║  ██║██║  ██║██╗
                 ╚══╝╚══╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝
            
                        Welcome to War!

                Type 'Start' to begin playing.
       If you don't know the rules, simply type 'rules'!

              For more help, type 'help' or '?'.

            """
    prompt = "> "
    game = Game()

    #Commands that let the user play the game
    def do_start(self, arg):
        """
        Starts the game.
        """
        while True:
            try:
                mode = int(input("Pick gamemode (1) for singleplayer, (2) for two-player: "))
                if mode == 1 or mode == 2:
                    break
                else:
                    print("Please enter either (1) or (2).")
            except:
                print("Please enter either (1) or (2).")

        player1 = input("Please enter the name of player 1: ")
        if mode == 2:
            player2 = input("Please enter the name of player 2: ")
            self.game.start(mode, player1, player2)
        else:
            self.game.start(mode, player1)
        
        start_txt = """
              
           You are now free to begin drawing cards!
             Use the command 'draw' or 'draw_card'
          
                    """
        print(start_txt)
        
        

    def do_draw_card(self, arg):
        """
        Draws a card from your deck.
        Will not work unless a game has been started using the 'start' command.
        """
        if self.game.get_active_game():
            self.game.draw_cards()
        else:
            print("Please start a game before you begin drawing cards!")

    def do_draw(self, arg):
        """Draws a card from your deck."""
        self.do_draw_card(arg)

    def do_cheat(self, arg):
        """Shh! This function will let you cheat in the game."""
        self.game.cheat()

    #Commands that give functionality to the game
    def do_rules(self, arg):
        """Prints the rules of War."""
        rules_text = """

        War card game rules:
        - The goal is to win all the cards.
        - The deck is divided evenly between two players.
        - Each player reveals the top card.
            - The higher card wins both cards.
        - Aces are high. Suits don't matter.
        - If the cards are equal, a 'war' occurs:
            - Each player places one card face down.
            - Each player then places then one card face up.
            - The higher face-up card wins all cards on the table.
            - If again tied, repeat the war.
        - The game continues until one player has all cards.
        - This is a simple game of chance with no strategy.

            """
        print(rules_text)
    
    def do_highscores(self, arg):
        """Prints a list of all Highscores!"""
        self.game.show_highscore()

    #TODO Better way to implement?
    def do_namechange(self, arg):
        """
        Lets the User/s change names.
        Will not work unless a game has been started using the 'start' command.
        """
        if self.game.get_active_game():
                name_to_replace = input("Please enter the name you would like to change: ")
                replacing_name = input(f"Please enter the name you would like to change {name_to_replace} to: ")
                self.game.name_change(name_to_replace, replacing_name)
        else:
            print("Please start a game before you begin drawing cards!")

    #Commands to quit the game
    def do_quit(self, arg):
        """Saves and closes the game."""
        print("Saving and Quitting the war game.")
        self.game.save_highscore()
        return True
    
    def do_q(self, arg):
        """Saves and closes the game."""
        return self.do_quit(arg)
    
    def do_exit(self, arg):
        """Saves and closes the game."""
        return self.do_quit(arg)
    
    def do_EOF(self, arg):
        """Saves and closes the game."""
        return self.do_quit(arg)