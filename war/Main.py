try: #Try imports for executing Main normally
    from Shell import Shell
except: #Except imports for UnitTesting. To prevent module not found Error.
    from .Shell import Shell 


class Main:
    """The Main Program When it runs"""

    def run(self):
        """Runs the main program"""
        
        Shell().cmdloop()


if __name__ == "__main__":
    Main().run()