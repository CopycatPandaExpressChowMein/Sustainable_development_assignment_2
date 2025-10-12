class Shell:
    """ handles the interface of the game, input and output. """

    def __init__(self):
        """ initialises the class named shell and
        with intro and prompt."""
        self.intro = " Welcome to WAR!!!"
        self.prompt = "Enter comand"

    def do_start(self):
        """ Start the game when using comand"""
        print("Starts the game.")

    def do_nameChange(self):
        """ changes name of player from shell when using comand"""
        print("Change the name of the player. ")

    def do_drawCard(self):
        """ Draws card when youser uses this comand."""
        print("Draws the card.")

    def do_quit(self):
        """ Quits the game whe using this comand and exits from shell."""
        print("Quit the war game.")

    def do_pickmode(self):
        """ Allows player to pick a mode from the shell interface."""
        print("Pick the mode of the game: ")

    def do_viewStatistics(self):
        """Displays the statistic to the user how they performed."""
        print("Vew the statistics ")

    def do_printRules(self):
        """ prints the rules of the game to the user."""
        print("Print out the rules of War.")

    def do_cheat(self):
        """ lets the you cheat in the game and triggers from shell """
        print("Cheat in War")
