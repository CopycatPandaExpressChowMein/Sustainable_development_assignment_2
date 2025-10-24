import unittest, datetime
from war.Statistics import Statistics


class TestStatistics(unittest.TestCase):

    def setUp(self):
        self.date = datetime.date.today()
        self.stat = Statistics(False, 21, self.date)

    def test_set_has_won(self):
        """Checks whether the set_has_won function correctly sets the has_won bool."""
        self.assertEqual(self.stat.set_has_won(True), True)

    def test_set_draws(self):
        """Checks whether the set_draws function correctly sets the number of draws."""
        self.assertEqual(self.stat.set_draws(4), 4)

    def test_set_date(self):
        """Checks whether the set_date function correctly sets the date."""
        new_date = datetime.date(2001, 1, 1)
        self.assertEqual(self.stat.set_date(new_date), new_date)

    def test_get_has_won(self):
        """Checks whether the get_has_won function correctly returns the state of the has_won bool"""
        self.assertEqual(self.stat.get_has_won(), False)

    def test_get_draws(self):
        """Checks whether the get_draws function correctly returns the value of the draws variable"""
        self.assertEqual(self.stat.get_draws(), 21)

    def test_get_date(self):
        """Checks whether the get_date function correctly retuns the value of the date variable"""
        self.assertEqual(self.stat.get_date(), self.date)


if __name__ == "__main__":
    unittest.main()
