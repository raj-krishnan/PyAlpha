from pyalpha.portfolio.models import setup_portfolio_database


class Portfolio:

    def __init__(self, name="", initial_balance=20000):
        self.name = name
        self.balance = initial_balance
        setup_portfolio_database()

    def get_stock_quote(self, symbol):
        """
        Get the current price of a stock
        """
        pass

    def buy_stock(self, symbol, quantity):
        """
        Buy a stock
        """
        pass

    def sell_stock(self, symbol, quantity):
        """
        Sell a stock
        """
        pass

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
