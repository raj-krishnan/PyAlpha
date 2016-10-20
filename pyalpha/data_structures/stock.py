import ystockquote


class StockNotFoundException(Exception):
    pass


class Stock:
    def __init__(self, symbol="TSLA"):
        self.symbol = symbol
        self.price = 0

    def __repr__(self):
        return self.symbol

    def __str__(self):
        return self.symbol

    def fetch_price(self):
        price = ystockquote.get_price(self.symbol)
        if price == 'N/A':
            raise StockNotFoundException
        else:
            self.price = float(price)
