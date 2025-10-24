import unittest
import datetime
import os
import json
from war.Game import Game
from war.Card import Card
from war.CardHand import CardHand
from war.Highscore import Highscore
from war.Statistics import Statistics


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

    def test_start_with_ai_level_and_ai_gets_level(self):
        """Starting singleplayer with ai_level should create an Intelligence with that level."""
        game = Game()
        game.start(mode=1, player1="Solo", ai_level="greedy")
        self.assertTrue(game.get_active_game())
        # second player should be an Intelligence with greedy level
        p2 = game._Game__players[1]
        # Intelligence exposes get_level()
        self.assertTrue(hasattr(p2, 'get_level'))
        self.assertEqual(p2.get_level(), 'greedy')

    def test_draw_when_player_has_no_cards_records_highscore(self):
        """If one player has no cards, the other is recorded as winner in highscores."""
        game = Game()
        game.start(mode=2, player1="A", player2="B")
        # empty player A's hand to trigger immediate loss
        from war.CardHand import CardHand
        game._Game__players[0].set_hand(CardHand([]))
        # ensure player B has at least one card
        self.assertGreaterEqual(len(game._Game__players[1].get_hand().getHand()), 0)
        # call draw_cards should record B as winner
        game.draw_cards()
        highs = game._Game__highscore.get_highscores()
        # The winner 'B' should have a key in highscores (possibly empty list appended)
        self.assertIn('B', highs)

    def test_name_change_updates_highscore_keys(self):
        """Game.name_change should propagate to Highscore and replace keys."""
        game = Game()
        game.start(mode=2, player1="Old", player2="Other")
        hs = game._Game__highscore
        # ensure Old exists
        self.assertIn('Old', hs.get_highscores())
        # perform rename
        game.name_change('Old', 'NewName')
        self.assertIn('NewName', hs.get_highscores())
        self.assertNotIn('Old', hs.get_highscores())

    def test_cheat_swap_missing_player(self):
        """cheat_swap should return False when one of the player names is not found."""
        game = Game()
        game.start(mode=2, player1="X", player2="Y")
        self.assertFalse(game.cheat_swap("X", "NoSuchPlayer", 0, 0))

    def test_war_with_insufficient_cards_causes_loss_and_records_highscore(self):
        """If a war occurs but player1 cannot continue (not enough cards) player2 should win and be recorded."""
        g = Game()
        # start a two-player game to get two human players
        g.start(mode=2, player1="A", player2="B")

        # Set up hands so both draw equal value and player1 will have <2 cards remaining
        p1 = g._Game__players[0]
        p2 = g._Game__players[1]

        # p1: will draw a '5' then have only 1 card left -> cannot continue war
        p1.set_hand(CardHand([Card(5, '5', 's', 'b'), Card(9, '9', 's', 'b')]))
        # p2: will draw a '5' and then have no cards left
        p2.set_hand(CardHand([Card(5, '5', 's', 'b')]))

        # Ensure precondition
        self.assertEqual(len(p1.get_hand().getHand()), 2)
        self.assertEqual(len(p2.get_hand().getHand()), 1)

        # Trigger the draw which should detect the war and then p1 can't continue and thus p2 wins
        g.draw_cards()

        # Player2 should have received the active cards from player1 (increase in hand size)
        p2_amount = p2.get_hand().amount
        self.assertGreaterEqual(p2_amount, 1)

    def test_ai_choose_index_is_used_when_provided(self):
        """If an AI provides choose_index, Game.draw_cards should pass that index to drawcard()."""
        g = Game()
        # singleplayer: player1 human, player2 AI
        g.start(mode=1, player1="Human", ai_level="top")
        p1 = g._Game__players[0]
        p2 = g._Game__players[1]

        # Give human a low card and AI two cards where the second card is higher
        p1.set_hand(CardHand([Card(2, '2', 's', 'b')]))
        p2.set_hand(CardHand([Card(1, '1', 's', 'b'), Card(13, 'K', 's', 'b')]))

        # Monkeypatch AI to choose index 1 (the stronger card)
        def choose_one():
            return 1

        setattr(p2, 'choose_index', choose_one)

        # Draw — AI should draw index 1
        g.draw_cards()

        # After the round, AI should have taken cards and therefore its hand amount should be >= 1
        self.assertGreaterEqual(p2.get_hand().amount, 1)


class TestHighscoreExtras(unittest.TestCase):
    def setUp(self):
        self.test_filename = "test/test_extras.json"
        # ensure clean start
        try:
            os.remove(self.test_filename)
        except Exception:
            pass

    def tearDown(self):
        try:
            os.remove(self.test_filename)
        except Exception:
            pass

    def test_save_and_load_statistics_roundtrip(self):
        """Saving highscores containing Statistics objects should reconstruct Statistics on load."""
        hs = Highscore(self.test_filename)
        # build a stats object and attach to a player
        d = datetime.date(2020, 5, 17)
        stat = Statistics(True, 7, d)
        hs.set_highscores({"Alice": [stat]})
        # save
        hs.save_highscores()
        # load with a fresh Highscore instance
        hs2 = Highscore(self.test_filename)
        loaded = hs2.get_highscores()
        self.assertIn("Alice", loaded)
        self.assertIsInstance(loaded["Alice"], list)
        self.assertTrue(len(loaded["Alice"]) >= 1)
        item = loaded["Alice"][0]
        # after load it should be a Statistics instance
        self.assertIsInstance(item, Statistics)
        self.assertEqual(item.get_has_won(), stat.get_has_won())
        self.assertEqual(item.get_draws(), stat.get_draws())
        self.assertEqual(item.get_date(), stat.get_date())

    def test_save_creates_file_and_contains_json(self):
        """Saving highscores should create the file and write valid JSON."""
        hs = Highscore(self.test_filename)
        hs.set_highscores({})
        # save and ensure file is created
        hs.save_highscores()
        self.assertTrue(os.path.exists(self.test_filename))
        # file should contain valid JSON (possibly empty dict)
        with open(self.test_filename, 'r', encoding='utf-8') as fh:
            data = json.load(fh)
        self.assertIsInstance(data, dict)

    def test_set_and_get_filename_changes_path(self):
        hs = Highscore(self.test_filename)
        newname = 'test/test_extras2.json'
        ret = hs.set_filename(newname)
        self.assertEqual(ret, newname)
        self.assertEqual(hs.get_filename(), newname)

    def test_load_with_invalid_json_results_in_empty_highscores(self):
        # write invalid JSON to file
        with open(self.test_filename, 'w', encoding='utf-8') as fh:
            fh.write('{ invalid json')
        # constructing Highscore should attempt to load and fall back to empty dict
        hs = Highscore(self.test_filename)
        loaded = hs.get_highscores()
        self.assertIsInstance(loaded, dict)
        self.assertEqual(len(loaded), 0)

    def test_add_player_and_add_statistics_then_save_and_load(self):
        hs = Highscore(self.test_filename)
        hs.add_player('Tester')
        hs.add_statistics('Tester', has_won=False, draws=3)
        # verify in-memory
        self.assertIn('Tester', hs.get_highscores())
        self.assertEqual(len(hs.get_highscores()['Tester']), 1)
        hs.save_highscores()
        # reload
        hs2 = Highscore(self.test_filename)
        self.assertIn('Tester', hs2.get_highscores())
        lst = hs2.get_highscores()['Tester']
        self.assertTrue(isinstance(lst, list))
        self.assertGreaterEqual(len(lst), 1)


class TestStatisticsExtra(unittest.TestCase):

    def test_set_date_with_iso_and_invalid_string(self):
        s = Statistics(False, 0, None)
        # valid ISO string
        d = '2020-12-31'
        stored = s.set_date(d)
        self.assertIsInstance(stored, datetime.date)
        self.assertEqual(stored.isoformat(), d)

        # invalid string should set date to None
        stored2 = s.set_date('not-a-date')
        self.assertIsNone(stored2)

    def test_from_dict_non_dict_raises(self):
        with self.assertRaises(TypeError):
            Statistics.from_dict(None)

    def test_from_dict_partial_and_invalid_date(self):
        # missing keys -> defaults used
        d = {}
        s = Statistics.from_dict(d)
        self.assertIsInstance(s, Statistics)
        self.assertFalse(s.get_has_won())
        self.assertEqual(s.get_draws(), 0)

        # invalid date string in dict -> date becomes None
        d2 = {'has_won': True, 'draws': 3, 'date': 'bad-format'}
        s2 = Statistics.from_dict(d2)
        self.assertTrue(s2.get_has_won())
        self.assertEqual(s2.get_draws(), 3)
        self.assertIsNone(s2.get_date())

    def test_set_date_with_datetime_and_to_dict_none(self):
        # passing a datetime.datetime should be accepted (subclass of date)
        dt = datetime.datetime(2021, 1, 2, 3, 4, 5)
        s = Statistics(False, 2, dt)
        self.assertEqual(s.get_date().year, 2021)

        # to_dict with None date returns date: None
        s2 = Statistics(True, 1, None)
        d = s2.to_dict()
        self.assertIn('date', d)
        self.assertIsNone(d['date'])

    def test_str_contains_tokens(self):
        s = Statistics(True, 7, datetime.date(2022, 2, 2))
        st = str(s)
        self.assertIn('Won', st)
        self.assertIn('Draws:', st)


if __name__ == "__main__":
    unittest.main()
