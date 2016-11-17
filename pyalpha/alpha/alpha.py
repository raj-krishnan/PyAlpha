import datetime
from abc import ABC, abstractmethod

import ystockquote
import numpy as np
import copy

from pyalpha.data_structures.historical_stock import HistoricalStock


class Alpha(ABC):
    def __init__(self, stock_list, start_date, end_date, cache_data=True,
                 use_cached_data=True):

        self.start_date = start_date
        self.end_date = end_date
        self.stock_list = stock_list
        self.data = {}
        self.use_cached_data = use_cached_data
        self.cache_data = cache_data

        self.funds = 10000000
        self.turnover = [0]
        self.returns = []

    def construct_historical_data(self):
        """
        Creates a data structure of historical stock data
        The data structure is a dictionary which maps the dates to
        a list of HistoricalStock instances, which contain the stock's
        data on the given date for each stock in the stock list.

        cache_data: Cache the resultant data using pickle
        use_cache: Use cached data if available
        Stock lists are user defined
        Stock lists for SNP100 and SNP500 available in stock_lists.py
        """
        for stock in self.stock_list:
            response = ystockquote.get_historical_prices(stock, self.start_date,
                                                         self.end_date)
            print(stock)
            for date_str, value in response.items():
                h = HistoricalStock(stock, date_str)
                h.set_data(value)
                d = date_str.split("-")
                date = datetime.date(int(d[0]), int(d[1]), int(d[2]))
                if date not in self.data.keys():
                    self.data[date] = []
                self.data[date].append(h)
        self.verify_historical_data()

    def verify_historical_data(self):
        stock_count = []
        for key in self.data.keys():
            stock_count.append(len(self.data[key]))
        max_len = max(stock_count)
        to_delete = []
        for key in self.data.keys():
            if len(self.data[key]) < max_len:
                to_delete.append(key)
        for key in to_delete:
            self.data.pop(key)

    @abstractmethod
    def alpha(self, stock):
        """
        Abstract Method: Needs to be defined by the user
        Sets the weight for each stock
        All parameters available in HistoricalStock can be used in here
        Returns a single decimal giving the weight of a stock
        """
        pass

    def simulate(self):
        """
        Runs the simulation for the user-defined alpha
        Calculates the cumulative return, drawdown, turnover
        """
        self.turnover = [0]
        self.returns = []
        stock_vector_old = None
        days = []
        for key in self.data.keys():
            days.append(key)

        days = sorted(days)
        print(days)
        for i in range(1, len(days)):
            data_day = days[i-1]
            trading_day = days[i]
            print(data_day)

            alpha_stock = []
            stock_prices_open = []
            stock_prices_close = []

            # Use the information obtained on the previous day to make
            # trades on the present day. Stocks are purchased when the
            # exchange opens and are sold as it closes.

            for stock in self.data[data_day]:
                alpha_stock.append(self.alpha(stock))
            for stock in self.data[trading_day]:
                stock_prices_open.append(stock.open)
                stock_prices_close.append(stock.close)

            alpha_total = sum(alpha_stock)
            stock_vector = []
            returns_day = 0

            for j in range(len(alpha_stock)):
                quantity = int(alpha_stock[j] * self.funds
                               / (alpha_total * stock_prices_open[j]))
                stock_vector.append(quantity)
                return_on_stock = ((stock_prices_close[j] - stock_prices_open[j])
                                   * quantity)
                self.data[trading_day][j].returns = return_on_stock
                returns_day += return_on_stock

            self.returns.append(returns_day)

            if stock_vector_old is not None:
                turnover_day = np.dot(stock_vector, stock_vector_old)
                self.turnover.append(turnover_day)
            stock_vector_old = stock_vector

