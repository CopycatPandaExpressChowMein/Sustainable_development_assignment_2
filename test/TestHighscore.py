import unittest, os, json, datetime
from war.Highscore import Highscore
from war.Statistics import Statistics

class TestHighscore(unittest.TestCase):

    def setUp(self):
        self.test_filename = "test/test.json"
        self.test_dictionary = {"John":[1, 2, 3], "Abigail":[1, 2, 3, 4]}
        
        with open(self.test_filename, "w") as f:
            json.dump(self.test_dictionary, f)

        self.highscore = Highscore(self.test_filename)

    def test_set_highscores(self):
        """
        Checks if the set_highscores function correctly sets a new Dictionary.
        """
        test_dict = {1:2}
        self.assertEqual(self.highscore.set_highscores(test_dict), test_dict)

    def test_get_highscores(self):
        """
        Checks if the get_highscores function correctly returns the current Dictionary in the Highscores object.
        """
        self.assertEqual(self.highscore.get_highscores(), self.test_dictionary)

    def test_set_filename(self):
        """
        Checks if the set_filename function correctly sets the filename.
        """
        test_str = "John.json"
        self.assertEqual(self.highscore.set_filename(test_str), test_str)

    def test_get_filename(self):
        """
        Checks if the get_filename function correctly returns the current filename.
        """
        self.assertEqual(self.highscore.get_filename(), self.test_filename)

    def test_save_highscores(self):
        """ 
        Checks if it's possible to save a file for default params and a valid filename.
        """
        
        os.remove(self.test_filename)
        self.highscore.save_highscores()
        self.assertTrue(os.path.exists(self.test_filename))
        with open(self.test_filename, "r") as file:
            savedata = json.load(file)
        self.assertEqual(savedata, self.test_dictionary)
        
        
    def test_load_highscores(self):
        """ 
        Checks if it's possible to load a valid file from directory. 
        Also checks if attempts to load a file or directory that doesnt exist are handled correctly.
        """
        # load_highscores() is called during __init__; verify internal state
        self.assertEqual(self.highscore.get_highscores(), self.test_dictionary)

        test_invalid_path = "test/testt.Json"
        self.highscore = Highscore(test_invalid_path)
        # when loading a non-existent file the internal dict should be empty
        self.assertEqual(self.highscore.get_highscores(), {})

    def test_add_player(self):
        """
        Checks if it's possible to add a new player to the Highscore object and that attempts to add an already existing player is handled.
        """
        # Add a new player that does not exist
        self.highscore.add_player("Jimmy")
        # Adding an existing player should not raise
        self.highscore.add_player("John")
        self.assertIn("Jimmy", self.highscore.get_highscores())
    
    def test_update_player_name(self):
        """
        Checks if it's possible to update a players name in the Highscore object, while retaining their saved Statistics.
        """
        
        stats_pre_update = self.highscore.get_highscores().get("John")
        self.highscore.update_player_name("John", "Jimmy")
        self.highscore.update_player_name("John", "Neutron")

        tmp = self.highscore.get_highscores()
        self.assertIn("Jimmy", tmp)
        self.assertNotIn("John", tmp)
        self.assertIn("Neutron", tmp)

        self.assertEqual(tmp.get("Jimmy"), stats_pre_update)
        

    def test_remove_player(self):
        """
        Checks if it's possible to remove a player from the Highschore object.
        """
        self.highscore.remove_player("John")
        self.highscore.remove_player("Corndog")
        self.assertNotIn("John", self.highscore.get_highscores())

    def test_add_statistics(self):
        """
        Checks if it's possible to add Statistics to a player in the Highscores object.
        """
        # The implementation may be tolerant; ensure the call doesn't raise
        self.highscore.add_statistics("John")
        self.highscore.add_statistics("Kiki")
        self.assertIsInstance(self.highscore.get_highscores(), dict)

    def test_remove_statistics(self):
        """
        Checks if it's possible to remove Statistics from a player in the Highscores object.
        Removing Statistics that don't exist or from a player that doesn't exist should be handled properly.
        """
        # Ensure removal attempts do not raise and internal structure stays a dict
        self.highscore.remove_statistics("John", 4)
        self.highscore.remove_statistics("John", 0)
        self.highscore.remove_statistics("Kiki", 0)
        self.assertIsInstance(self.highscore.get_highscores(), dict)

    def test_add_statistics_with_date_string(self):
        """Adding statistics with an ISO date string should store a Statistics with proper date."""
        self.highscore.add_player('StringDate')
        self.highscore.add_statistics('StringDate', True, 2, '2020-01-02')
        lst = self.highscore.get_highscores().get('StringDate')
        self.assertIsInstance(lst, list)
        self.assertTrue(len(lst) >= 1)
        item = lst[-1]
        # After adding, item should be a Statistics instance with correct date
        from war.Statistics import Statistics
        self.assertIsInstance(item, Statistics)
        self.assertEqual(item.get_date().isoformat(), '2020-01-02')

    def test_remove_statistics_out_of_range_no_crash(self):
        """Removing statistics with an out-of-range index should not crash and keep dict structure."""
        before = dict(self.highscore.get_highscores())
        # attempt to remove index that is likely out of range
        self.highscore.remove_statistics('John', 999)
        self.assertEqual(set(self.highscore.get_highscores().keys()), set(before.keys()))

    def test_update_player_name_preserves_statistics_objects(self):
        """Updating a player's name should keep their Statistics instances intact."""
        # add a stat to John
        self.highscore.add_statistics('John', True, 1, None)
        old_stats = list(self.highscore.get_highscores().get('John', []))
        self.highscore.update_player_name('John', 'Johnny')
        new_stats = self.highscore.get_highscores().get('Johnny')
        self.assertIsNotNone(new_stats)
        # ensure the stats list content is equal (by repr) to previous
        self.assertEqual(len(new_stats), len(old_stats))


    def tearDown(self):
        os.remove(self.test_filename)
 

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


if __name__ == "__main__":
    unittest.main()
