class Statistics:
    """
    Object that stores information about game statistics.
    With the required methods to manipulate that information.
    """

    def __init__(self, has_won=False, draws=0, date=None):
        """
        Initializes the object to given arguments.
        Uses class functions.

        :has_won: Boolean indicating if a game was won. Default param is False.
        :draws: Integer representing how many draws where done in a game. Default param is 0.
        :date: The date the game was played as a datettime object. Default param is None.
        """
        self.set_has_won(has_won)
        self.set_draws(draws)
        self.set_date(date)

    def __str__(self):
        """
        Defines how to represent the object as a String.
        Prints the value of all variables in a presentable format.
        """
        print(
            f"Match: {"Won" if self.__has_won == True else "Lost"} | Draws: {self.__draws}"
        )

    def set_has_won(self, has_won):
        """
        Sets the has_won bool to the given argument.
        
        :has_won: Boolean indicating if a game was won. 
        """
        self.__has_won = has_won
        return self.__has_won

    def set_draws(self, draws):
        """
        Sets the draws variable to the given argument.

        :draws: Integer representing how many draws where done in a game.
        """
        self.__draws = draws
        return self.__draws

    def set_date(self, date):
        """
        Sets the date variable to the given argument.'
        
        :date: The date the game was played as a datettime object.
        """
        self.__date = date
        return self.__date

    def get_has_won(self):
        """
        Returns if a game was won as a boolean.
        """
        return self.__has_won

    def get_draws(self):
        """
        Returns the number of draws in the game as an int.
        """
        return self.__draws

    def get_date(self):
        """
        Returns the date when the game was played.
        """
        return self.__date
