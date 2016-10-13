import ystockquote


class Stock:
    def __init__(self, symbol="TSLA"):
        self.symbol = symbol
        self.price = 0

    def fetch_price(self):
        self.price = float(ystockquote.get_price(self.symbol))

    def __repr__(self):
        return self.symbol

    def __str__(self):
        return self.symbol
