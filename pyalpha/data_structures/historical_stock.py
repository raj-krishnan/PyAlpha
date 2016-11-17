import ystockquote


class HistoricalStock:
    def __init__(self, symbol="TSLA", date="2016-10-12"):
        self.symbol = symbol
        self.date = date

        self.adj_close = 0
        self.close = 0
        self.high = 0
        self.low = 0
        self.open = 0
        self.volume = 0
        self.returns = 0

    def __repr__(self):
        return self.symbol

    def __str__(self):
        return self.symbol

    def fetch_prices(self):
        data = ystockquote.get_historical_prices(self.symbol, self.date, self.date)[self.date]
        self.set_data(data)

    def set_data(self, data):
        self.adj_close = float(data['Adj Close'])
        self.close = float(data['Close'])
        self.high = float(data['High'])
        self.low = float(data['Low'])
        self.open = float(data['Open'])
        self.volume = float(data['Volume'])
