import unittest, os, json
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
        self.assertEqual(self.highscore.load_highscores(), self.test_dictionary)

        test_invalid_path = "test/testt.Json"
        self.highscore = Highscore(test_invalid_path)
        self.assertEqual(self.highscore.load_highscores(), {})

    def test_add_player(self):
        """
        Checks if it's possible to add a new player to the Highscore object and that attempts to add an already existing player is handled.
        """
        self.highscore.add_player("John")
        self.highscore.add_player("Jimmy")
        self.highscore.add_player()
        self.assertIn("Jimmy", self.highscore.get_highscores())
        self.assertIn("Anonymous", self.highscore.get_highscores())
    
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
        self.assertNotIn("Neutron", tmp)

        self.assertEqual(tmp.get("Jimmy"), stats_pre_update)
        self.assertEqual(tmp.get("Neutron"), [])
        

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
        old_len = len(self.highscore.get_highscores().get("John"))
        self.highscore.add_statistics("John")
        self.highscore.add_statistics("Kiki")
        self.assertGreater(len(self.highscore.get_highscores().get("John")), old_len)

    def test_remove_statistics(self):
        """
        Checks if it's possible to remove Statistics from a player in the Highscores object.
        Removing Statistics that don't exist or from a player that doesn't exist should be handled properly.
        """
        old_stats = len(self.highscore.get_highscores().get("John"))
        self.highscore.remove_statistics("John", 4)
        self.highscore.remove_statistics("John", 0)
        self.highscore.remove_statistics("Kiki", 0)
        self.assertLess(len(self.highscore.get_highscores().get("John")), 3)


    def tearDown(self):
        os.remove(self.test_filename)

if __name__ == "__main__":
    unittest.main()
