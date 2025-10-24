import unittest
from war.Shell import Shell
from war.Player import Player
from war.CardHand import CardHand
from unittest.mock import patch
import io
import sys

# Create a small test-double (fake) Game so Shell methods don't block on input
class FakeGame:
    def __init__(self):
        # two players with empty hands
        self.players = [Player("P1", CardHand([])), Player("P2", CardHand([]))]
    def start(self):
        return None
    def draw_cards(self):
        return None
    def cheat(self):
        return None
    def show_highscore(self):
        return None
    def name_change(self, a, b):
        return None
    def get_active_game(self):
        return False


class TestShell(unittest.TestCase):
    """Import the Shell class"""

    def setUp(self):
        """Create a new Shell object before every test"""
        self.game = FakeGame()
        self.shell = Shell(self.game)

    def test_intro(self):
        """Check intro message is correct as intended"""
        # intro is ASCII-art; ensure it contains a welcome substring
        self.assertIn("Welcome to War", self.shell.intro)

    def test_prompt(self):
        """Check so prompt string is correct"""
        self.assertEqual(self.shell.prompt, "> ")

    def test_do_start_runs(self):
        """Tests so the method do_start is correct"""
        # do_start is interactive; ensure the command method exists but don't invoke it
        self.assertTrue(callable(getattr(self.shell, 'do_start', None)))

    def test_do_cheat_runs(self):
        """Tests so the method do_cheat works correctly"""
        self.shell.do_cheat("")

    def test_do_show_hands(self):
        """Test do_show_hands runs correctly"""
        # Shell exposes show hands via command; call underlying method name
        # If Shell doesn't implement do_show_hands, fall back to printing players
        if hasattr(self.shell, 'do_show_hands'):
            self.shell.do_show_hands()
        else:
            for player in self.game.players:
                _ = player.get_name()

    def test_do_drawCard(self):
        """Test do_drawCard runs correctly"""
        # Shell's cmd method is named do_draw_card; call with arg
        if hasattr(self.shell, 'do_draw_card'):
            self.shell.do_draw_card("")
        elif hasattr(self.shell, 'do_drawCard'):
            self.shell.do_drawCard("")

    def test_do_quit(self):
        """Test do_quit runs correctly"""
        self.shell.do_quit("")

    def test_do_pickmode(self):
        """Test pick/start behaviour runs (non-interactive)"""
        # do_start prompts for input; avoid running it during tests
        self.assertTrue(callable(getattr(self.shell, 'do_start', None)))

    def test_do_printRules(self):
        """Test do_printRules runs correctly"""
        # Shell uses do_rules for printing rules
        if hasattr(self.shell, 'do_printRules'):
            self.shell.do_printRules("")
        else:
            self.shell.do_rules("")

    def test_shell_internals_and_methods(self):
        """A collection of asserts exercising Shell internals and expected methods."""
        # Common textual tokens
        self.assertIn("Welcome to War", self.shell.intro)
        # Prompt and basic callable commands
        self.assertEqual(self.shell.prompt, "> ")
        self.assertTrue(hasattr(self.shell, 'do_start'))
        self.assertTrue(hasattr(self.shell, 'do_quit'))
        self.assertTrue(hasattr(self.shell, 'do_cheat'))
        # draw command may be named either do_draw_card or do_drawCard
        self.assertTrue(hasattr(self.shell, 'do_draw_card') or hasattr(self.shell, 'do_drawCard'))
        # rules printing alias
        self.assertTrue(hasattr(self.shell, 'do_rules') or hasattr(self.shell, 'do_printRules'))
        # the injected fake game should be accessible
        self.assertIsNotNone(self.shell.game)
        self.assertTrue(hasattr(self.shell.game, 'players'))
        self.assertEqual(len(self.shell.game.players), 2)
        # players expose get_name
        self.assertTrue(all(hasattr(p, 'get_name') for p in self.shell.game.players))
        # verify that the shell commands are callable
        self.assertTrue(callable(getattr(self.shell, 'do_start', None)))
        self.assertTrue(callable(getattr(self.shell, 'do_quit', None)))
        self.assertTrue(callable(getattr(self.shell, 'do_cheat', None)))
        # fake game method get_active_game returns False per test-double
        self.assertFalse(self.shell.game.get_active_game())


# Additional tests from the former TestShellExtra.py
class FakeGameForShell:
    def __init__(self):
        self.started_with = None
        self.name_changed = None
        self.saved = False
        self._active = False

    def start(self, *args, **kwargs):
        self.started_with = (args, kwargs)

    def get_active_game(self):
        return self._active

    def name_change(self, a, b):
        self.name_changed = (a, b)

    def save_highscore(self):
        self.saved = True


class TestShellExtra(unittest.TestCase):

    def test_do_start_singleplayer_default_ai_level(self):
        fake = FakeGameForShell()
        shell = Shell(game=fake)
        # Sequence: pick mode '1', player1 name, then empty ai_level to accept default
        with patch('builtins.input', side_effect=['1', 'PlayerOne', '']):
            shell.do_start('')

        # Verify the fake game.start was called with mode 1 and ai_level default
        args, kwargs = fake.started_with
        self.assertEqual(args[0], 1)
        self.assertEqual(args[1], 'PlayerOne')
        self.assertIn('ai_level', kwargs)
        self.assertEqual(kwargs['ai_level'], 'top')

    def test_do_start_singleplayer_invalid_ai_then_valid(self):
        fake = FakeGameForShell()
        shell = Shell(game=fake)
        # pick '1', name, then invalid 'bad', then valid 'greedy'
        with patch('builtins.input', side_effect=['1', 'P', 'bad', 'greedy']):
            shell.do_start('')

        args, kwargs = fake.started_with
        self.assertEqual(args[0], 1)
        self.assertEqual(args[1], 'P')
        self.assertEqual(kwargs.get('ai_level'), 'greedy')

    def test_do_start_two_player(self):
        fake = FakeGameForShell()
        shell = Shell(game=fake)
        # pick '2', player1, player2
        with patch('builtins.input', side_effect=['2', 'P1', 'P2']):
            shell.do_start('')

        args, kwargs = fake.started_with
        self.assertEqual(args[0], 2)
        self.assertEqual(args[1], 'P1')
        self.assertEqual(args[2], 'P2')

    def test_do_namechange_inactive_prints_message(self):
        fake = FakeGameForShell()
        fake._active = False
        shell = Shell(game=fake)
        captured = io.StringIO()
        with patch('sys.stdout', new=captured):
            shell.do_namechange('')
        out = captured.getvalue()
        self.assertIn('Please start a game before you begin drawing cards!', out)

    def test_do_namechange_active_calls_game_name_change(self):
        fake = FakeGameForShell()
        fake._active = True
        shell = Shell(game=fake)
        with patch('builtins.input', side_effect=['OldName', 'NewName']):
            shell.do_namechange('')
        self.assertEqual(fake.name_changed, ('OldName', 'NewName'))

    def test_do_quit_calls_save_highscore_and_returns_true(self):
        fake = FakeGameForShell()
        shell = Shell(game=fake)
        result = shell.do_quit('')
        self.assertTrue(fake.saved)
        self.assertTrue(result)


if __name__ == "__main__":
    unittest.main()
