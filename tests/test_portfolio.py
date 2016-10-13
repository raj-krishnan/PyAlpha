import unittest

from pyalpha.data_structures.HistoricalStock import HistoricalStock
from pyalpha.data_structures.Stock import Stock


class PortfolioTest(unittest.TestCase):
    def setUp(self):
        pass

    def test_stock_price_fetch(self):
        tesla = Stock()
        tesla.fetch_price()
        self.assertTrue(tesla.price > 0)

    def test_historical_price_fetch(self):
        tesla_historical = HistoricalStock()
        tesla_historical.fetch_prices()
        self.assertTrue(tesla_historical.high >= tesla_historical.low)
        self.assertTrue(tesla_historical.low > 0)

    def tearDown(self):
        pass
