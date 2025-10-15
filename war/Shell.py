from war.Game import Game


class Shell:
    """handles the interface of the game, input and output."""

    def __init__(self, game):
        """initialise the shell with intro, prompt and link to the Game"""
        self.intro = "Welcome to WAR!!!"
        self.prompt = "Enter command"
        self.game = game

    def do_start(self):
        """Start the game when using command"""
        self.game.start()

    def do_nameChange(self):
        """changes name of player from shell when using command"""
        print("Change the name of the player.")

    def do_drawCard(self):
        """Draws card when user uses this command"""
        print("Draws the card.")

    def do_quit(self):
        """Quits the game when using command"""
        print("Quit the war game.")

    def do_pickmode(self):
        """Allows player to pick a mode from the shell interface"""
        print("Standard War card game - Human vs AI only.")

    def do_viewStatistics(self):
        """Displays the statistics how player performed"""
        print("View the statistics.")

    def do_printRules(self):
        """prints the rules of the game to the user"""
        rules_text = """
            War card game rules:
            - The goal is to win all the cards.
            - The deck is divided evenly between two players.
            - Each player reveals the top card.
            The higher card wins both cards.
            - Aces are high. Suits don't matter.
            - If the cards are equal, a 'war' occurs:
            Each player places one card face down, then one card face up.
            The higher face-up card wins all cards on the table.
            If again tied, repeat the war.
            - The game continues until one player has all cards.
            - If a player runs out of cards during a war,
            some variants say they lose immediately.
            - This is a simple game of chance with no strategy.
            """
        print(rules_text)

    def do_cheat(self):
        """lets you cheat in the game and triggers from shell"""
        self.game.cheat()
