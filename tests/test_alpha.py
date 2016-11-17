import unittest

from pyalpha.alpha.alpha import Alpha
import pyalpha.alpha.stock_lists as stock_lists


class AlphaDataset(Alpha):
    def alpha(self, stock):
        return 1.0


class TestAlpha(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        start_date = "2015-01-02"
        end_date = "2015-01-08"
        cls.alpha = AlphaDataset(stock_lists.SNP100,
                                 start_date,
                                 end_date)

    def test_dataset_creation_snp100(self):
        TestAlpha.alpha.construct_historical_data()
        keys = list(TestAlpha.alpha.data.keys())

        self.assertEqual(len(keys), 5)

        self.assertEqual(len(TestAlpha.alpha.data[keys[0]]),
                         len(TestAlpha.alpha.data[keys[1]]))

        self.assertLess(5, len(TestAlpha.alpha.data[keys[0]]))

        for stock in TestAlpha.alpha.data[keys[0]]:
            self.assertLess(0.0, stock.close)

        self.assertEqual(len(TestAlpha.alpha.data[keys[0]]),
                         len(stock_lists.SNP100))

    def test_simulation(self):
        TestAlpha.alpha.simulate()
        for i in TestAlpha.alpha.returns:
            self.assertTrue(i != 0)
