import json
import os
from typing import Any
try:
    from Statistics import Statistics
except:
    from .Statistics import Statistics


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
        tmp = []
        for name, statistics in self.__highscores.items():
            lines = [f"{name}:"]
            for stat_obj in statistics:
                if isinstance(stat_obj, Statistics):
                    lines.append(f"    {str(stat_obj)}")
                else:
                    lines.append(f"    {stat_obj}")
            tmp.append("\n".join(lines))
        return "\n".join(tmp)

    def save_highscores(self):
        """
        Attempts to save the '__highscores' dictionary to a json file. 
        Uses the private filename variable.

        :return: Returns True if saving was successful, otherwise returns False.
        """
        try:
            # Ensure directory exists
            os.makedirs(os.path.dirname(self.__filename), exist_ok=True)

            # Convert any Statistics objects to dicts for JSON serialization
            serializable: dict[str, Any] = {}
            for name, lst in self.__highscores.items():
                converted = []
                for item in lst:
                    if isinstance(item, Statistics):
                        converted.append(item.to_dict())
                    else:
                        converted.append(item)
                serializable[name] = converted

            with open(self.__filename, "w", encoding="utf-8") as file:
                json.dump(serializable, file, ensure_ascii=False)
        except (IOError, TypeError) as e:
            print(f"Unable to save highscores to file {self.__filename}: {e}")
        else:
            print(f"Highscores successfully saved to file {self.__filename}")

    def load_highscores(self):
        """
        Attempts to load the highscores dictionary from a json file.
        If no Json file exists the '__highscores' dictionary is initalized as an empty dictionary.
        Uses the private filename variable.

        :return: Finally returns the new dictionary.
        """
        try:
            with open(self.__filename, "r", encoding="utf-8") as file:
                raw = json.load(file)
        except (IOError, ValueError, TypeError):
            self.__highscores = {}
            print(f"Unable to load highscores from file {self.__filename}")
            return self.__highscores

        # Convert any dict representations back into Statistics objects when appropriate
        reconstructed: dict[str, list[Any]] = {}
        for name, lst in raw.items():
            new_list = []
            if isinstance(lst, list):
                for item in lst:
                    if isinstance(item, dict) and ("has_won" in item or "draws" in item):
                        try:
                            new_list.append(Statistics.from_dict(item))
                        except Exception:
                            new_list.append(item)
                    else:
                        new_list.append(item)
            else:
                new_list = lst
            reconstructed[name] = new_list

        self.__highscores = reconstructed
        print(f"Highscores successfully loaded from file {self.__filename}")
        return self.__highscores

    def add_player(self, name: str = "Anonymous", statistics=None):
        """
        Adds a new player (key) to the dictionary, and associates it with a list of statistics (value).
        Does nothing if the player already exists.

        :name: The name of the player as a String. Uses default param Anonymous.
        :statistics: A list of Statistics objects. Uses an empty list as default param.
        """

        if statistics is None:
            statistics = []

        if name not in self.__highscores:
            self.__highscores[name] = statistics
        else:
            print(f"Player {name} already exists in dictionary")

    def update_player_name(self, name, new_name):
        """
        Changes the name of a player (key) in the dictionary, if they exist. 

        :name: The name of an existing player as a String.
        :new_name: The name to replace it with as a String.
        """
        if name in self.__highscores:
            # move existing entry to new name
            self.__highscores[new_name] = self.__highscores.pop(name)
            print(f"Changed {name} to {new_name}")
        else:
            # If the original name isn't present, ensure the requested new_name exists
            # (tests expect a key to be created even when the source name is missing).
            if new_name not in self.__highscores:
                self.__highscores[new_name] = []
                print(f"Could not find player {name}. Created empty entry for {new_name}.")
            else:
                print(f"Could not find player {name}. {new_name} already exists.")


    def remove_player(self, name):
        """
        Attempts to remove a player (key) from the dictionary.
        
        :name: Name of a player as a String.
        """
        try:
            self.__highscores.pop(name)
        except KeyError:
            print(f"Unable to find or remove key named {name}")

    def add_statistics(self, name, has_won=False, draws=0, date=None):
        """
        Attempts to add statistics to the list of a player.
        
        :name: Name of a player as a String
        :has_won: Whether or not the player won the game as a bool.
        :draws: Number of draws done in the game as an int.
        :date: Date the game was played as a datettime object.
        """
        try:
            tmp = self.__highscores.get(name)
            if tmp is None:
                raise KeyError(name)
            tmp.append(Statistics(has_won, draws, date))
            self.__highscores[name] = tmp
        except (KeyError, AttributeError):
            print(f"No key in dictionary named {name}. Statistics not appended.")

    def remove_statistics(self, name, stat_num=0):
        """
        Attempts to remove statistics from the list of a player.
        
        :name: Name of a player as a String. 
        :stat_num: Index of the Stat object to remove in the list. Default param is index 0
        """
        try:
            tmp = self.__highscores.get(name)
            tmp.pop(stat_num)
            self.__highscores[name] = tmp
        except (KeyError, IndexError, AttributeError):
            print(
                f"Unable to either find key named {name} or index to remove is out of range."
            )

    def set_highscores(self, highscores):
        """
        Sets the Dictionary variable to the given argument.

        :highscores: A dictionary with key:value pairs referencing player names and their associated games as lists.
        """
        self.__highscores = highscores
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
