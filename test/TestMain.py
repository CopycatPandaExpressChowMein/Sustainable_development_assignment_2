import unittest
from war.Main import Main  # if needed

class TestMain(unittest.TestCase):
    """ Tests for Main program """

    def test_run_prints(self):
        """ Test the run method runs and prints """
        main = Main()
        main.run()

if __name__ == "__main__":
    unittest.main()
