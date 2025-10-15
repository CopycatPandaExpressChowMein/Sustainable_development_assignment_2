import unittest
from war.Shell import Shell
from war.Game import Game  # if you create/use Game inside tests


class TestShell(unittest.TestCase):
    """ Import the Shell class """

    def setUp(self):
        """ Create a new Shell object before every test """
        self.game = Game()
        self.shell = Shell(self.game)

    def test_intro(self):
        """ Check intro message is correct as intended """
        self.assertEqual(self.shell.intro.strip(), "Welcome to WAR!!!")

    def test_prompt(self):
        """ Check so prompt string is correct """
        self.assertEqual(self.shell.prompt, "Enter command")

    def test_do_start_runs(self):
        """ Tests so the method do_start is correct """
        self.shell.do_start()

    def test_do_cheat_runs(self):
        """ Tests so the method do_cheat works correctly """
        self.shell.do_cheat()

    def test_do_nameChange(self):
        """ Test do_nameChange runs correctly """
        self.shell.do_nameChange()

    def test_do_drawCard(self):
        """ Test do_drawCard runs correctly """
        self.shell.do_drawCard()

    def test_do_quit(self):
        """ Test do_quit runs correctly """
        self.shell.do_quit()

    def test_do_pickmode(self):
        """ Test do_pickmode runs correctly """
        self.shell.do_pickmode()

    def test_do_viewStatistics(self):
        """ Test do_viewStatistics runs correctly """
        self.shell.do_viewStatistics()

    def test_do_printRules(self):
        """ Test do_printRules runs correctly """
        self.shell.do_printRules()


if __name__ == "__main__":
    unittest.main()
