"""Command-line Shell for the War game.

This module implements a small interactive CLI using cmd.Cmd. The Shell class
is thin: it accepts a Game (or a test-double) via its constructor so logic is
testable without running an interactive loop.
"""

import cmd
try: #Try imports for executing Main normally
    from Game import Game
except: #Except imports for UnitTesting. To prevent module not found Error.
    from .Game import Game

#TODO Rework cheat to be more aligned with requirements, "cheat that one can use for testing purposes and reach the end of the game faster"
#TODO Rework Graphical interface

class Shell(cmd.Cmd):
    """Command-line interface shell for the War game."""
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

    def __init__(self, game=None):
        """Initialize the Shell and optionally inject a Game instance for tests."""
        super().__init__()
        self.game = game if game is not None else Game()

    #Commands that let the user play the game
    def do_start(self, arg):
        """Start a new interactive game by prompting for mode and names."""
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
            # Ask for AI intelligence level when starting singleplayer mode
            while True:
                ai_level = input("Choose AI level ('top', 'random', 'greedy') [top]: ").strip().lower()
                if ai_level == "":
                    ai_level = "top"
                if ai_level in ("top", "random", "greedy"):
                    break
                print("Invalid choice. Please select 'top', 'random' or 'greedy'.")
            self.game.start(mode, player1, ai_level=ai_level)
        
        start_txt = """
              
           You are now free to begin drawing cards!
             Use the command 'draw' or 'draw_card'
          
                    """
        print(start_txt)
        
        

    def do_draw_card(self, arg):
        """Draw one round in the active game.

        Prints a helpful message if no game is active.
        """
        if self.game.get_active_game():
            self.game.draw_cards()
        else:
            print("Please start a game before you begin drawing cards!")

    def do_draw(self, arg):
        """Alias for `draw_card`."""
        self.do_draw_card(arg)

    def do_cheat(self, arg):
        """Trigger the game's cheat hook (used by tests or for debug)."""
        self.game.cheat()

    #Commands that give functionality to the game
    def do_rules(self, arg):
        """Print the rules of the War card game."""
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
        """Display stored highscores by delegating to the Game object."""
        self.game.show_highscore()

    #TODO Better way to implement?
    def do_namechange(self, arg):
        """Change a player's name in the active game and persist highscores.

        Prompts interactively for the existing and replacement names.
        """
        if self.game.get_active_game():
                name_to_replace = input("Please enter the name you would like to change: ")
                replacing_name = input(f"Please enter the name you would like to change {name_to_replace} to: ")
                self.game.name_change(name_to_replace, replacing_name)
        else:
            print("Please start a game before you begin drawing cards!")

    #Commands to quit the game
    def do_quit(self, arg):
        """Save highscores (best-effort) and exit the shell."""
        print("Saving and Quitting the war game.")
        # Attempt to save highscores if the Game-like object supports it.
        if hasattr(self.game, 'save_highscore') and callable(getattr(self.game, 'save_highscore')):
            try:
                self.game.save_highscore()
            except Exception:
                # Don't let save errors break quitting; best-effort only.
                pass
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