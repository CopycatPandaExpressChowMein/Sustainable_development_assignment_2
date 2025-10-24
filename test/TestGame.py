import unittest
from war.Game import Game


class TestGame(unittest.TestCase):
    """Tests for Game logic"""

    def test_initial_mode(self):
        """Game should initialize with the correct mode"""
        # Current Game implementation exposes get_active_game() and starts programmatically
        game = Game()
        self.assertFalse(game.get_active_game())

    def test_pickmode_runs(self):
        """Pickmode runs without crashing (non-interactive)"""
        game = Game()
        # Start a singleplayer game programmatically to ensure start works
        game.start(mode=1, player1="Alice")
        self.assertTrue(game.get_active_game())

    def test_start_two_player(self):
        """Starting a two-player game should set two human players."""
        game = Game()
        game.start(mode=2, player1="A", player2="B")
        # Confirm active and player names
        self.assertTrue(game.get_active_game())
        players = [p.get_name() for p in game._Game__players]
        self.assertIn("A", players)
        self.assertIn("B", players)

    def test_draw_once_reduces_hand_and_increments_draws(self):
        """Drawing once should increment the draw counter and reduce each hand by at most one."""
        game = Game()
        game.start(mode=1, player1="Alice")
        # record initial sizes
        h0 = len(game._Game__players[0].get_hand().getHand())
        h1 = len(game._Game__players[1].get_hand().getHand())
        game.draw_cards()
        self.assertEqual(game.num_draws, 1)
        # At least one player's hand has decreased (or game ended)
        new_h0 = len(game._Game__players[0].get_hand().getHand())
        new_h1 = len(game._Game__players[1].get_hand().getHand())
        self.assertTrue(new_h0 < h0 or new_h1 < h1 or not game.get_active_game())

    def test_cheat_swap_success_and_failure(self):
        """Test that cheat_swap exchanges cards when indices are valid and rejects invalid indices."""
        game = Game()
        game.start(mode=2, player1="P1", player2="P2")

        p1_hand = game._Game__players[0].get_hand().getHand()
        p2_hand = game._Game__players[1].get_hand().getHand()

        # Ensure both hands have at least one card for the test
        self.assertGreaterEqual(len(p1_hand), 1)
        self.assertGreaterEqual(len(p2_hand), 1)

        # Record top cards
        p1_top_before = p1_hand[0]
        p2_top_before = p2_hand[0]

        # Successful swap of top cards
        ok = game.cheat_swap("P1", "P2", 0, 0)
        self.assertTrue(ok)

        p1_hand_after = game._Game__players[0].get_hand().getHand()
        p2_hand_after = game._Game__players[1].get_hand().getHand()

        self.assertIs(p1_hand_after[0], p2_top_before)
        self.assertIs(p2_hand_after[0], p1_top_before)

        # Out of range indices should fail and leave hands unchanged
        before_p1 = list(p1_hand_after)
        before_p2 = list(p2_hand_after)
        self.assertFalse(game.cheat_swap("P1", "P2", 999, 0))
        self.assertEqual(before_p1, game._Game__players[0].get_hand().getHand())
        self.assertEqual(before_p2, game._Game__players[1].get_hand().getHand())


if __name__ == "__main__":
    unittest.main()
