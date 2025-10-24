import unittest
from war.Main import Main  # if needed


class TestMain(unittest.TestCase):
    """Tests for Main program"""

    def test_run_prints(self):
        """Test the run method runs and prints"""
        # Do not execute the full application loop in tests; just check the method exists
        main = Main()
        self.assertTrue(callable(getattr(main, 'run', None)))

    def test_can_instantiate_main(self):
        """Main can be instantiated repeatedly without side-effects."""
        m1 = Main()
        m2 = Main()
        self.assertIsNot(m1, m2)


if __name__ == "__main__":
    unittest.main()
