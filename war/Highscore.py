import json
from war.Statistics import Statistics

class Highscore:
    """ Object that handles loading, saving and management of game statistics.
        Uses a private dictionary to store highscores, each key is related to a list of Statistics objects."""


    def __init__(self, filename = "war/highscores.json"):
        """ Initializes a Highscore object, 
            and calls for the 'load_highscores()' method to retrieve a dictionary from a json file"""
        self.__filename = filename
        self.load_highscores()
    
    def __str__(self):
        """ Defines how to represent the object as a String."""
        for name, statistics in self.__highscores:
            print(f"{name}: ")
            for stat_obj in statistics:
                print(f"    {stat_obj}")

    def save_highscores(self):
        """ Attempts to save the '__highscores' dictionary to a json file, uses a String as an argument.
            The String should be a filename ending in .json, default 'FILENAME' is used if no argument is given."""
        try:
            with open(self.__filename, "w") as file:
                json.dump(self.__highscores, file)
        except IOError:
            print(f"Unable to save highscores to file {self.__filename}")
        else:
            print(f"Highscores successfully saved to file {self.__filename}")

    def load_highscores(self):
        """ Attempts to load the highscores dictionary from a json file, uses a String as an argument.
            The String should be a filename ending in .json, default 'FILENAME' is used if no argument is given.
            If no Json file exists the '__highscores' dictionary is initalized as an empty dictionary."""
        try:
            with open(self.__filename, "r") as file:
                self.__highscores = json.load(file)
        except IOError:
            self.__highscores = {}
            print(f"Unable to load highscores from file {self.__filename}")
        else:
            print(f"Highscores successfully loaded from file {self.__filename}")

    def add_player(self, name, statistics=[]):
        """ Adds a new key using the argument name to the dictionary, then calls for 'save_highscores()'.
            Takes a list as an argument, otherwise uses an empty list by default.
            The list should contain objects of type Statistics.
            Does nothing if the key already exists.
            """

        if name not in self.__highscores:
            self.__highscores[name] = statistics
            self.save_highscores()
        else:
            print(f"Player {name} already exists in dictionary")

    def update_player_name(self, name, new_name):
        """ Attempts to move the value of key 'name' to a new key 'new_name'.
            Takes 'name' and 'new_name' as arguments, 'name' should be a player name.
            """
        try:
            self.__highscores[new_name] = self.__highscores.pop(name)
        except KeyError:
            print(f"No key in dictionary named {name}. Making new key.")
            self.__highscores[new_name] = []
        finally:
            self.save_highscores()

    def remove_player(self, name):  
        """ Attempts to remove key 'name' if it exists. 
            Uses String as an argument, which should be the name of a player.
            """
        try:
            self.__highscores.pop(name)
            self.save_highscores()
        except KeyError:
            print(f"Unable to find or remove key named {name}")

    def add_statistics(self, name, has_won=False, draws=0):
        """ Attempts to add statistics to the list of a key 'name' if it exists. 
            Then calls for 'save_highscores()'
            Takes String, boolean and an int as arguments, the bool and int are used to make a new statistics object.
            The String should be the name of a player, the boolean if the player has won the game and the int the number of draws it took.
            """
        try:
            self.__highscores[name] = self.__highscores.get(name).append(Statistics(has_won, draws))
            self.save_highscores()
        except KeyError:
            print(f"No key in dictionary named {name}. Statistics not appended.")

    def remove_statistics(self, name, stat_num):
        """ Attempts to remove statistics from the list of a key 'name' if it exists.
            Then calls for 'save_highscores()'
            Takes a String as an argument, which should be the name of a player.
            And an integer 'stat_num' which should be the index of the item you want to remove."""
        try:
            self.__highscores[name] = self.__highscores.get(name).pop(stat_num)
            self.save_highscores()
        except (KeyError, IndexError):
            print(f"Unable to either find key named {name} or index to remove is out of range.")

    def set_highscores(self, highscores):
        """ Takes a dictionary as an argument, and sets the private variable '__highscores' to that dictionary.
            Then calls for 'save_highscores()'"""
        self.__highscores = highscores
        self.save_highscores()
        return self.__highscores

    def get_highscores(self):
        """Returns the private variable '__highscores' as a dictionary"""
        return self.__highscores
    
    def set_filename(self, filename):
        """ Takes a String as an argument and sets the private variable filename to the value of that string,
            the String should be the filename you want to save or load from."""
        self.__filename = filename
        return self.__filename
    
    def get_filename(self):
        """Returns the currently used filename that the class saves to."""
        return self.__filename
    
    
    

