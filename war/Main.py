try:
    from Shell import Shell
except:
    from .Shell import Shell


class Main:
    """The Main Program When it runs"""

    def run(self):
        """Runs the main program"""
        
        Shell().cmdloop()


if __name__ == "__main__":
    Main().run()