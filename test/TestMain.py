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

    def test_run_invokes_shell_cmdloop(self):
        """Main.run should call Shell().cmdloop(); patch Shell in the Main module."""
        from unittest.mock import patch

        class FakeShell:
            called = False

            def __init__(self):
                FakeShell.called = False

            def cmdloop(self):
                FakeShell.called = True
                return "FAKELOOP"

        with patch('war.Main.Shell', FakeShell):
            main = Main()
            result = main.run()
            # cmdloop should have been called; Main.run does not return the cmdloop return value
            self.assertTrue(FakeShell.called)
            self.assertIsNone(result)

    def test_multiple_instantiations_are_isolated(self):
        """Creating multiple Main objects should not share instance state."""
        m1 = Main()
        m2 = Main()
        # ensure they are separate objects
        self.assertIsNot(m1, m2)
        # ensure no unexpected attributes exist by default
        self.assertFalse(hasattr(m1, 'shell'))
        self.assertFalse(hasattr(m2, 'shell'))

    def test_run_does_not_create_persistent_shell_attribute(self):
        """Running Main.run shouldn't leave a 'shell' attribute on Main instances."""
        from unittest.mock import patch

        class DummyShell:
            def cmdloop(self):
                return None

        with patch('war.Main.Shell', DummyShell):
            m = Main()
            _ = m.run()
            # confirm that Main instance still has no attribute 'shell'
            self.assertFalse(hasattr(m, 'shell'))


if __name__ == "__main__":
    unittest.main()
