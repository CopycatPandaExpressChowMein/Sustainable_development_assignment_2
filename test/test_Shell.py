import unittest
from war.Shell import Shell
"""Import the Shell class"""


class TestShell(unittest.TestCase):
    def setUp(self):
        """Create a new Shell object before every test"""
        self.shell = Shell()

    def test_intro(self):
        """check intro massage is correct as intended"""
        self.assertEqual(self.shell.intro.strip(), "Welcome to WAR!!!")

    def test_prompt(self):
        """chekc so promt string is correct"""
        self.assertEqual(self.shell.prompt, "Enter comand")

    def test_do_start_runs(self):
        """ tests so the method do_start is correct"""
        self.shell.do_start()

    def test_do_nameChange_runs(self):
        """tests so do_namChange method is correct """
        self.shell.do_nameChange()

    def test_do_drawCard_runs(self):
        """ tests so do_drawCard method works correct """
        self.shell.do_drawCard()

    def test_do_quit_runs(self):
        """test so do_quit metod works correct """
        self.shell.do_quit()

    def test_do_pickmode_runs(self):
        """ test so the do_pickmode method works correctly"""
        self.shell.do_pickmode()

    def test_do_viewStatistics_runs(self):
        """ test so do_viestatistics method works correctly """
        self.shell.do_viewStatistics()

    def test_do_printRules_runs(self):
        """ test do_printRules works corretly """
        self.shell.do_printRules()

    def test_do_cheat_runs(self):
        """ test do_cheat method works correctly """
        self.shell.do_cheat()


if __name__ == "__main__":
    unittest.main()
