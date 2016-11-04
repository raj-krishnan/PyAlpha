import unittest

from pyalpha.alpha.alpha import Alpha
import pyalpha.alpha.stock_lists as stock_lists


class AlphaDataset(Alpha):
    def alpha(self, stock):
        return 1.0


class TestAlpha(unittest.TestCase):
    def test_dataset_creation_snp100(self):
        alpha = AlphaDataset()

        start_date = "2015-01-02"
        end_date = "2015-01-08"
        alpha.construct_historical_data(stock_lists.SNP100,
                                        start_date,
                                        end_date)
        keys = list(alpha.data.keys())

        self.assertEqual(len(keys), 5)

        self.assertEqual(len(alpha.data[keys[0]]), len(alpha.data[keys[1]]))

        self.assertLess(5, len(alpha.data[keys[0]]))

        for stock in alpha.data[keys[0]]:
            self.assertLess(0.0, stock.close)

        self.assertEqual(len(alpha.data[keys[0]]), len(stock_lists.SNP100))
