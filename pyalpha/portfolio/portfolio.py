from pyalpha.portfolio import models
from pyalpha.data_structures.Stock import Stock


class Portfolio:

    def __init__(self, name="", initial_balance=20000):
        self.name = name
        self.balance = initial_balance
        # is this line correct (that is we are calling this function every time
        # that we add a new person)
        models.setup_portfolio_database()
        models.TablePerson.insert(name=self.name).execute()

    def get_stock_quote(self, symbol):
        """
        Get the current price of a stock
        """
        stock = Stock(symbol)
        stock.fetch_price()
        return stock.price

    def buy_stock(self, symbol, quantity):
        """
        Buy a stock
        """
        stock_price = self.get_stock_quote(symbol)
        new_stock = models.TablePortfolio(
            name=self.name, stock=symbol,
            purchase_price=stock_price, quantity=quantity)
        new_stock.save()
        self.balance = self.balance - stock_price * quantity

    def sell_stock(self, symbol, quantity):
        """
        Sell a stock
        """
        stock_price = self.get_stock_quote(symbol)
        models.TablePortfolio.select().where(
            models.TablePortfolio.person == self.name).exists()
        new_stock = models.TablePortfolio(
            person=self.name, stock=symbol,
            purchase_price=stock_price, quantity=quantity)
        new_stock.save()
        self.balance = self.balance - stock_price * quantity

    def view_portfolio(self):
        """
        View list of stocks owned, their quantities and value
        """
        pass

    def get_transaction_history(self):
        """
        Get list of transactions made from log file
        """
        pass

    def add_funds(self, deposit):
        """
        Increase balance in the account
        """
        self.balance += deposit

    def logger(self, action, symbol, cost, quantity, balance):
        """
        Logs all actions performed: BUY, SELL, ADD_FUNDS
        Format:
        Date | Time | Action | Symbol | Cost | Quantity | Amount | Balance
        """
        pass
