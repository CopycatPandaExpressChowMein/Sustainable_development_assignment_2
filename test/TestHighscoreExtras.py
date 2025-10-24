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
