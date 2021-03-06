import unittest
import ystockquote
import tempfile

from pyalpha.alpha import Alpha
import pyalpha.alpha.stock_lists as stock_lists


class AlphaDataset(Alpha):
    def alpha(self, stock):
        return 1.0/stock.close


class TestAlpha(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.start_date = "2015-01-02"
        cls.end_date = "2016-11-19"
        cls.alpha = AlphaDataset(stock_lists.SNP100,
                                 cls.start_date,
                                 cls.end_date)
        cls.temp_dir = tempfile.gettempdir()

    def test_load_data_file_not_exists(self):
        self.assertIsNone(TestAlpha.alpha.load_data())

    def test_dataset_creation_snp100(self):
        TestAlpha.alpha.construct_historical_data()
        keys = list(TestAlpha.alpha.data.keys())

        # self.assertEqual(len(keys), 252)

        self.assertEqual(len(TestAlpha.alpha.data[keys[0]]),
                         len(TestAlpha.alpha.data[keys[1]]))

        self.assertLess(5, len(TestAlpha.alpha.data[keys[0]]))

        for stock in TestAlpha.alpha.data[keys[0]]:
            self.assertLess(0.0, stock.close)

        self.assertEqual(len(TestAlpha.alpha.data[keys[0]]),
                         len(stock_lists.SNP100))

    def test_execution(self):
        TestAlpha.alpha.simulate()
        for i in TestAlpha.alpha.returns:
            self.assertTrue(i != 0)

    def test_result_against_snp100(self):
        data = ystockquote.get_historical_prices("^OEX",
                                                 TestAlpha.start_date,
                                                 TestAlpha.end_date)
        return_snp100 = 0
        for k, v in data.items():
            open_price = float(v["Open"])
            close = float(v["Close"])
            return_snp100 += (close / open_price - 1) * 100

        return_pyalpha = sum(TestAlpha.alpha.returns)
        print(return_pyalpha)
        print(return_snp100)
        self.assertLess(abs(return_pyalpha - return_snp100), 7.5)

    def test_save_and_load_data(self):
        TestAlpha.alpha.save_data("test_stock_data.pickle",
                                  TestAlpha.temp_dir)
        to_compare_Alpha = AlphaDataset(stock_lists.SNP100,
                                        TestAlpha.start_date,
                                        TestAlpha.end_date)
        to_compare_Alpha.load_data("test_stock_data.pickle",
                                   TestAlpha.temp_dir)
        to_compare_Alpha.simulate()
        self.assertEqual(TestAlpha.alpha.returns, to_compare_Alpha.returns)

    def test_save_data_file_already_exists(self):
        self.assertIsNone(TestAlpha.alpha.save_data("test_stock_data.pickle",
                                                    TestAlpha.temp_dir))
