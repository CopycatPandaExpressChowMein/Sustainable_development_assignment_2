import json
from Statistics import Statistics


class Highscore:
    """
    Object that handles loading, saving and management of game statistics.
    Uses a private dictionary to store highscores, each key is related to a list of Statistics objects.
    """

    def __init__(self, filename="war/highscores.json"):
        """
        Initializes the Highscore object.
        Calls for the load_highscores() function to handle loading previous data based on the given filename.
        (Or creates a new Dict if there is file associated with the given filename)

        :filename: The filename to save and load to. Default is war/highscores.json.
        """
        self.__filename = filename
        self.load_highscores()

    def __str__(self):
        """
        Defines how to represent the object as a String.
        Loops through all names and statistics, printing each name, and their associated statistics beneath.
        """
        for name, statistics in self.__highscores:
            print(f"{name}: ")
            for stat_obj in statistics:
                print(f"    {stat_obj}")

    def save_highscores(self):
        """
        Attempts to save the '__highscores' dictionary to a json file. 
        Uses the private filename variable.

        :raises IOError: Raises IOError if an error occurs while trying to save. 
        """
        try:
            with open(self.__filename, "w") as file:
                json.dump(self.__highscores, file)
        except IOError:
            print(f"Unable to save highscores to file {self.__filename}")
        else:
            print(f"Highscores successfully saved to file {self.__filename}")

    def load_highscores(self):
        """
        Attempts to load the highscores dictionary from a json file.
        If no Json file exists the '__highscores' dictionary is initalized as an empty dictionary.
        Uses the private filename variable.

        :raises IOError: Raises an IOError if an error occurs while trying to load from a file.
        """
        try:
            with open(self.__filename, "r") as file:
                self.__highscores = json.load(file)
        except IOError:
            self.__highscores = {}
            print(f"Unable to load highscores from file {self.__filename}")
        else:
            print(f"Highscores successfully loaded from file {self.__filename}")

    def add_player(self, name="Anonymous", statistics=[]):
        """
        Adds a new player (key) to the dictionary, and associates it with a list of statistics (value).
        Does nothing if the player already exists.

        :name: The name of the player as a String. Uses default param Anonymous.
        :statistics: A list of Statistics objects. Uses an empty list as default param.
        """

        if name not in self.__highscores:
            self.__highscores[name] = statistics
            self.save_highscores()
        else:
            print(f"Player {name} already exists in dictionary")

    def update_player_name(self, name, new_name):
        """
        Changes the name of a player (key) in the dictionary, if they exist. 
        Adds them as a new player (key) with an empty list (value) if they do not.

        :name: The name of an existing player as a String.
        :new_name: The name to replace it with as a String.
        :raises KeyError: Raises a KeyError if the player name is an invalid key. 
        """
        try:
            self.__highscores[new_name] = self.__highscores.pop(name)
        except KeyError:
            print(f"No key in dictionary named {name}. Making new key.")
            self.__highscores[new_name] = []
        finally:
            self.save_highscores()

    def remove_player(self, name):
        """
        Attempts to remove a player (key) from the dictionary.
        
        :name: Name of a player as a String.
        :raises KeyError: Raises a KeyError if the player name is an invalid key. 
        """
        try:
            self.__highscores.pop(name)
            self.save_highscores()
        except KeyError:
            print(f"Unable to find or remove key named {name}")

    def add_statistics(self, name, has_won=False, draws=0, date=None):
        """
        Attempts to add statistics to the list of a player.
        
        :name: Name of a player as a String
        :has_won: Whether or not the player won the game as a bool.
        :draws: Number of draws done in the game as an int.
        :date: Date the game was played as a datettime object.
        :raises KeyError: Raises a KeyError if the player name is an invalid key. 
        """
        try:
            self.__highscores[name] = self.__highscores.get(name).append(
                Statistics(has_won, draws)
            )
            self.save_highscores()
        except KeyError:
            print(f"No key in dictionary named {name}. Statistics not appended.")

    def remove_statistics(self, name, stat_num):
        """
        Attempts to remove statistics from the list of a player.
        
        :name: Name of a player as a String. 
        :stat_num: Index of the Stat object to remove in the list.
        :raises KeyError: Raises a KeyError if the player name is an invalid key. 
        :raises IndexError: Raises an IndexError if there is no Stat obj for the given index.
        """
        try:
            self.__highscores[name] = self.__highscores.get(name).pop(stat_num)
            self.save_highscores()
        except (KeyError, IndexError):
            print(
                f"Unable to either find key named {name} or index to remove is out of range."
            )

    def set_highscores(self, highscores):
        """
        Sets the Dictionary variable to the given argument.

        :highscores: A dictionary with key:value pairs referencing player names and their associated games as lists.
        """
        self.__highscores = highscores
        self.save_highscores()
        return self.__highscores

    def get_highscores(self):
        """
        Returns the private variable '__highscores' as a dictionary
        """
        return self.__highscores

    def set_filename(self, filename):
        """
        Sets the filename variable to the given argument.,
        
        :filename: Filename for use with IO operations as a String. Should be of the format "{filename}.json".
        """
        self.__filename = filename
        return self.__filename

    def get_filename(self):
        """
        Returns the currently used filename that the class saves to.
        """
        return self.__filename
