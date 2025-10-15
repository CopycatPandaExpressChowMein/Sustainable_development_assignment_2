import unittest, datetime
from war.Statistics import Statistics


class TestStatistics(unittest.TestCase):

    def test_set_has_won(self):
        stat = Statistics()
        self.assertEqual(stat.set_has_won(True), True)

    def test_set_draws(self):
        stat = Statistics()
        self.assertEqual(stat.set_draws(47), 47)

    def test_set_date(self):
        stat = Statistics()
        tmp_date = datetime.date.today()
        self.assertEqual(stat.set_date(tmp_date), tmp_date)

    def test_get_has_won(self):
        stat = Statistics(True)
        self.assertEqual(stat.get_has_won(), True)

    def test_get_draws(self):
        stat = Statistics(False, 47)
        self.assertEqual(stat.get_draws(), 47)

    def test_get_date(self):
        tmp_date = datetime.date.today()
        stat = Statistics(False, 0, tmp_date)
        self.assertEqual(stat.get_date(), tmp_date)


if __name__ == "__main__":
    unittest.main()
