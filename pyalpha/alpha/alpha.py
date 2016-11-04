import datetime
from abc import ABC, abstractmethod

import ystockquote

from pyalpha.data_structures.historical_stock import HistoricalStock


class Alpha(ABC):
    def __init__(self):
        self.data = {}

    def construct_historical_data(self, stock_list, start_date, end_date,
                                  cache_data=1, use_cached_data=1):
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
        for stock in stock_list:
            response = ystockquote.get_historical_prices(stock, start_date,
                                                         end_date)
            for date_str, value in response.items():
                h = HistoricalStock(stock, date_str)
                h.set_data(value)
                d = date_str.split("-")
                date = datetime.date(int(d[0]), int(d[1]), int(d[2]))
                if date not in self.data.keys():
                    self.data[date] = []
                self.data[date].append(h)

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
        pass
