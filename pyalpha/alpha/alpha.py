from abc import ABC, abstractmethod


class Alpha(ABC):
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
        pass

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
