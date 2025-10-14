class Statistics:
    """ Object that stores information about game statistics.
        With the required methods to manipulate that information."""

    def __init__(self, has_won=False, draws=0, date = None):
        """ Initializes a Statistics object, takes a boolean and integer as a parameter. 
            Uses default paramaters 'False' and '0' if none are given."""
        self.set_has_won(has_won)
        self.set_draws(draws)
        self.set_date(date)
    
    def __str__(self):
        """ Defines how to represent the object as a String."""
        print(f"Match: {"Won" if self.__has_won == True else "Lost"} | Draws: {self.__draws}")
    
    def set_has_won(self, has_won):
        """ Takes a boolean as a argument and sets the private __has_won variable to that argument.
            The boolean should be whether or not a game was won."""
        self.__has_won = has_won
        return self.__has_won

    def set_draws(self, draws):
        """ Takes an integer as an argument and sets the private __draws variable to that argument.
            The integer should be the number of draws that were done in a game."""
        self.__draws = draws
        return self.__draws

    def set_date(self, date):
        """ Takes a datetime as an argument and sets the private __date variable to that argument,
            the date should be when the game was played."""
        self.__date = date
        return self.__date

    def get_has_won(self):
        """Returns if a game was won as a boolean."""
        return self.__has_won
    
    def get_draws(self):
        """Returns the number of draws in the game as an int."""
        return self.__draws
    
    def get_date(self):
        """Returns the date when the game was played."""
        return self.__date