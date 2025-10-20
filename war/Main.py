from Game import Game
from Shell import Shell

class Main:
    """The Main Program When it runs"""

    def run(self):
        """Runs the main program"""
        print("The Main program is running")

        game = Game()  
        shell = Shell(game)  
        shell.do_start()  
        print("The main program is running")
