from war.Game import Game
from war.Shell import Shell


class Main:
    """The Main Program When it runs"""

    def run(self):
        """Runs the main program"""
        print("The Main program is running")

        game = Game()  # Create a new game
        shell = Shell(game)  # Create shell interface linked to the game
        shell.run()  # Start the game using shell

        print("The main program is running")


if __name__ == "__main__":
    Main().run()