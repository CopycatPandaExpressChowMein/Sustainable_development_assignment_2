"""Highscore persistence module.

Provides the Highscore class used to load/save player statistics to JSON and
reconstruct Statistics objects on load. This module contains IO code and
serialization helpers used by Game and Shell.
"""

import json
import os
from typing import Any

try:
    from Statistics import Statistics
except:
    from .Statistics import Statistics


class Highscore:
    """Manage persistence and in-memory storage of player statistics.

    Stores highscores in a private dictionary mapping player names to lists
    of Statistics objects. Provides load/save and simple management helpers.
    """

    def __init__(self, filename="war/highscores.json"):
        """Initialize Highscore and load existing data from filename.

        :param filename: path to JSON file used for persistence
        """
        self.__filename = filename
        self.load_highscores()

    def __str__(self):
        """Return a human-readable representation of all highscores."""
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
        """Save highscores to the configured JSON file."""
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
        """Load highscores from JSON, returning an empty dict on failure."""
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
                    if isinstance(item, dict) and (
                        "has_won" in item or "draws" in item
                    ):
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
        """Add a player key to the highscores dict.

        If the player exists this is a no-op. `statistics` should be a list
        of Statistics objects or None.
        """

        if statistics is None:
            statistics = []

        if name not in self.__highscores:
            self.__highscores[name] = statistics
        else:
            print(f"Player {name} already exists in dictionary")

    def update_player_name(self, name, new_name):
        """Rename a player key while preserving their statistics.

        If `name` does not exist tests expect `new_name` to be created as an
        empty entry.
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
                print(
                    f"Could not find player {name}. Created empty entry for {new_name}."
                )
            else:
                print(f"Could not find player {name}. {new_name} already exists.")

    def remove_player(self, name):
        """Remove a player key from the highscores dictionary.

        Prints a message when the key is not present rather than raising.
        """
        try:
            self.__highscores.pop(name)
        except KeyError:
            print(f"Unable to find or remove key named {name}")

    def add_statistics(self, name, has_won=False, draws=0, date=None):
        """Append a Statistics record for the given player name.

        If the player key does not exist a message is printed and no-op is
        performed.
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
        """Remove a statistics entry at index `stat_num` for `name`.

        Safe: prints a message on KeyError/IndexError instead of raising.
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
        """Replace the in-memory highscores dictionary.

        :param highscores: dict mapping player names to lists of statistics
        """
        self.__highscores = highscores
        return self.__highscores

    def get_highscores(self):
        """Return the current highscores dictionary."""
        return self.__highscores

    def set_filename(self, filename):
        """Set the filename used for loading/saving highscores.

        :param filename: path to a JSON file
        :return: the stored filename
        """
        self.__filename = filename
        return self.__filename

    def get_filename(self):
        """Return the current highscores filename."""
        return self.__filename
