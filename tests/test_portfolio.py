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

    def test_get_stock_quote(self):
        pass

    def test_buy_stock_sufficient_balance(self):
        pass

    def test_buy_stock_insufficient_balance(self):
        pass

    def test_sell_stock_sufficient_stocks_available(self):
        pass

    def test_sell_stock_insufficient_stocks_available(self):
        pass

    def test_funds_deposit(self):
        pass

    def test_transaction_history(self):
        pass

    def test_portfolio_contents(self):
        pass

    def test_check_logs(self):
        pass

    def tearDown(self):
        pass
