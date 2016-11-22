import os
import unittest

from pyalpha.data_structures.historical_stock import HistoricalStock
from pyalpha.data_structures.stock import Stock
from pyalpha.portfolio.portfolio import StockExchange, InputError


class TestStockExchange(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.se = StockExchange()
        cls.rich = cls.se.add_user("Rich", 1000000)
        cls.poor = cls.se.add_user("Poor", 10)

    def test_add_user_initial_balance_to_be_positive(self):
        self.assertIsNone(TestStockExchange.se.add_user("John", -10))

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
        value = TestStockExchange.rich._get_stock_quote("TSLA")
        self.assertTrue(value > 0)

    def test_buy_stock_sufficient_balance(self):
        self.assertTrue(TestStockExchange.rich.buy_stock("AAPL", 2))
        self.assertTrue(TestStockExchange.rich.buy_stock("AAPL", 2))

    def test_buy_stock_insufficient_balance(self):
        self.assertRaises(InputError, TestStockExchange.poor.buy_stock,
                          "AAPL", 20)

    def test_sell_stock_sufficient_stocks_available(self):
        self.assertTrue(TestStockExchange.rich.sell_stock("AAPL", 1))

        # Sell all the stocks
        self.assertTrue(TestStockExchange.rich.sell_stock("AAPL", 3))
        # No stock available
        self.assertRaises(InputError, TestStockExchange.rich.sell_stock,
                          "AAPL", 1)


    def test_sell_stock_insufficient_stocks_available(self):
        self.assertRaises(InputError, TestStockExchange.rich.sell_stock,
                          "AAPL", 20)

    def test_sell_stock_stock_not_available(self):
        self.assertRaises(InputError, TestStockExchange.rich.sell_stock,
                          "GOOGL", 10)

    def test_funds_deposit(self):
        deposit = 1000
        balance = TestStockExchange.rich.balance
        TestStockExchange.rich.add_funds(deposit)
        self.assertEqual(balance + deposit, TestStockExchange.rich.balance)

    def test_funds_withdrawal(self):
        withdrawal = 1000
        balance = TestStockExchange.rich.balance
        self.assertRaises(InputError, TestStockExchange.rich.add_funds,
                          -1 * withdrawal)

        # Should not withdraw funds
        self.assertEqual(balance, TestStockExchange.rich.balance)

    def test_check_view_portfolio(self):
        self.assertTrue(len(TestStockExchange.rich.view_portfolio().axes[0]))

    def test_log_user_portfolio(self):
        self.assertTrue(len(TestStockExchange.rich.view_log().axes[0]))

    def test_log_stock_exchange(self):
        self.assertTrue(len(TestStockExchange.se.view_log().axes[0]))

    def test_log_stock_exchange_contains_all_user_logs(self):
        self.assertEqual(len(TestStockExchange.se.view_log().axes[0]),
                         len(TestStockExchange.rich.view_log().axes[0]) +
                         len(TestStockExchange.poor.view_log().axes[0]))

    @classmethod
    def tearDownClass(cls):
        try:
            os.remove("portfolio.db")
        except:
            return

if __name__ == '__main__':
    unittest.main()
