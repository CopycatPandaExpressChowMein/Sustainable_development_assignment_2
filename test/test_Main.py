import unittest
from war.Main import Main
""" impor Main class """


class TestMain(unittest.TestCase):
    def test_run_prints(self):
        main = Main()
        """Create a new Main object"""

        main.run()
        """Call the run() method to make sure it works properly"""


if __name__ == "__main__":
    unittest.main()
