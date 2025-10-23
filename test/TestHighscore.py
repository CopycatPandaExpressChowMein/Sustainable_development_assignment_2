import unittest, tempfile, os
from war.Highscore import Highscore
from war.Statistics import Statistics

class TestHighscore(unittest.TestCase):

    def setUp(self):
        # Create a temporary file to avoid using disk or default file
        self.test_file = tempfile.NamedTemporaryFile(delete=False)
        self.test_file.close()  # Close file so Highscore can open it
        self.hs = Highscore(filename=self.test_file.name)

    def tearDown(self):
        try:
            os.remove(self.test_file.name)
        except OSError:
            pass

    def test_save_highscores(self):
        self.hs.set_highscores({"player1": []})
        self.hs.save_highscores()
        with open(self.test_file.name, "r") as file:
            data = file.read()
        self.assertIn("player1", data)

    def test_load_highscores(self):
        self.hs.set_highscores({"player2": []})
        self.hs.save_highscores()
        # Create new instance to load from file
        hs2 = Highscore(filename=self.test_file.name)
        self.assertIn("player2", hs2.get_highscores())

    def test_add_player(self):
        self.hs.add_player("player3")
        self.assertIn("player3", self.hs.get_highscores())

    def test_update_player_name(self):
        self.hs.add_player("old_name")
        self.hs.update_player_name("old_name", "new_name")
        self.assertIn("new_name", self.hs.get_highscores())
        self.assertNotIn("old_name", self.hs.get_highscores())

    def test_remove_player(self):
        self.hs.add_player("player4")
        self.hs.remove_player("player4")
        self.assertNotIn("player4", self.hs.get_highscores())

    def test_add_statistics(self):
        self.hs.add_player("player5", [])
        self.hs.add_statistics("player5", has_won=True, draws=2)
        stats_list = self.hs.get_highscores().get("player5")
        self.assertTrue(any(stat.has_won for stat in stats_list))

    def test_remove_statistics(self):
        self.hs.add_player("player6", [Statistics(True, 3)])
        self.hs.remove_statistics("player6", 0)
        self.assertEqual(len(self.hs.get_highscores().get("player6")), 0)

    def test_set_highscores(self):
        new_scores = {"player7": []}
        self.hs.set_highscores(new_scores)
        self.assertEqual(new_scores, self.hs.get_highscores())

    def test_get_highscores(self):
        self.hs.set_highscores({"player8": []})
        scores = self.hs.get_highscores()
        self.assertIsInstance(scores, dict)
        self.assertIn("player8", scores)

    def test_set_filename(self):
        new_filename = "newfile.json"
        returned = self.hs.set_filename(new_filename)
        self.assertEqual(returned, new_filename)
        self.assertEqual(self.hs.get_filename(), new_filename)

    def test_get_filename(self):
        filename = self.hs.get_filename()
        self.assertIsInstance(filename, str)

if __name__ == "__main__":
    unittest.main()
