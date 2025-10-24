"""Additional Highscore tests (file I/O, round-trips and edge cases)."""
import unittest
import os
import json
import datetime

from war.Highscore import Highscore
from war.Statistics import Statistics


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
