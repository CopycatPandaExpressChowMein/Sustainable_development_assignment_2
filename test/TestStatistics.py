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

    def test_multiple_sets_and_gets(self):
        """Setters should return the set value and getters should reflect changes."""
        self.assertEqual(self.stat.set_has_won(True), True)
        self.assertTrue(self.stat.get_has_won())
        self.assertEqual(self.stat.set_draws(0), 0)
        self.assertEqual(self.stat.get_draws(), 0)
        new_date = self.stat.set_date(self.date)
        self.assertEqual(self.stat.get_date(), new_date)

    def test_independent_instances(self):
        """Multiple Statistics instances should maintain independent state."""
        s1 = Statistics(True, 1, self.date)
        s2 = Statistics(False, 2, None)
        self.assertTrue(s1.get_has_won())
        self.assertFalse(s2.get_has_won())
        s2.set_has_won(True)
        self.assertTrue(s2.get_has_won())

    def test_to_from_dict_roundtrip(self):
        """to_dict and from_dict should roundtrip preserving values."""
        s = Statistics(True, 5, self.date)
        d = s.to_dict()
        self.assertIsInstance(d, dict)
        s2 = Statistics.from_dict(d)
        self.assertEqual(s2.get_has_won(), s.get_has_won())
        self.assertEqual(s2.get_draws(), s.get_draws())
        self.assertEqual(s2.get_date(), s.get_date())


if __name__ == "__main__":
    unittest.main()
