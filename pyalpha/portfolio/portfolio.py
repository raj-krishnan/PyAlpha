import pandas

from pyalpha.portfolio import models
from pyalpha.data_structures.Stock import Stock


class Person():
    """
    Object with
    """

    def __init__(self, person_name, initial_balance):
        self.name = person_name
        self.balance = initial_balance

    def add_funds(self, deposit):
        """
        Increase balance in the account
        """
        self.balance = self.balance + deposit

    def get_stock_quote(self, symbol):
        """
        Get the current price of a stock
        """
        stock = Stock(symbol)
        stock.fetch_price()
        return stock.price

    def buy_stock(self, symbol, quantity):
        """
        Buy a given amount of a stock
        """
        stock_price = self.get_stock_quote(symbol)
        person_record = models.TablePerson.get(
            models.TablePerson.name == self.name)
        portfolio_record = (models.TablePortfolio
                            .select()
                            .where(models.TablePortfolio.person == person_record,
                                   models.TablePortfolio.stock == symbol))
        if portfolio_record.exists():
            new_average = (portfolio_record.average_price * portfolio_record.quantity +
                           stock_price * quantity) / (portfolio_record.quantity + quantity)
            # Modify entry in TablePortfolio
            portfolio_record.average_price = new_average
            portfolio_record.quantity = portfolio_record.quantity + quantity
            portfolio_record.save()
        else:
            new_average = stock_price
            # Add entry to TablePortfolio
            new_portfolio_record = models.TablePortfolio(
                person=person_record, stock=symbol,
                average_price=new_average, quantity=quantity)
            new_portfolio_record.save()

        # # Add/modify entry in TablePortfolio
        # new_portfolio_record = models.TablePortfolio(
        #     person=person_record, stock=symbol,
        #     average_price=new_average, quantity=quantity)
        # new_portfolio_record.save()

        # Update the balance of the person
        self.balance = self.balance - stock_price * quantity
        # Modify entry in TablePerson
        person_record.balance = self.balance
        person_record.save()

    def sell_stock(self, symbol, quantity):
        """
        Sell the specified amount of a stock
        """
        stock_price = self.get_stock_quote(symbol)
        person_record = models.TablePerson.get(
            models.TablePerson.name == self.name)
        portfolio_record = (models.TablePortfolio
                            .select()
                            .where(models.TablePortfolio.person == person_record,
                                   models.TablePortfolio.stock == symbol))
        if portfolio_record.exists():
            if quantity < portfolio_record.quantity:
                new_average = (portfolio_record.average_price * portfolio_record.quantity -
                               stock_price * quantity) / (portfolio_record.quantity - quantity)
            elif quantity == portfolio_record.quantity:
                new_average = 0
            # Modify entry in TablePortfolio
            portfolio_record.average_price = new_average
            portfolio_record.quantity = portfolio_record.quantity - quantity
            portfolio_record.save()

        # Modify entry in TablePortfolio
        # new_portfolio_record = models.TablePortfolio(
        #     person=person_record, stock=symbol,
        #     average_price=new_average, quantity=quantity)
        # new_portfolio_record.save()
        # Update the balance of the person
        self.balance = self.balance + stock_price * quantity
        # Modify entry in TablePerson
        person_record.balance = self.balance
        person_record.save()

    def get_transaction_history(self, user=""):
        """
        Get list of transactions made from log file
        """
        return self.log.loc[self.log['Name'] == user]


class Portfolio:

    def __init__(self):
        models.setup_portfolio_database()
        # Contains 'name of the person' as the key, with the 'People object' as
        # the value
        self.people = {}
        self.log = pandas.DataFrame()

    def add_person(self, person_name="", initial_balance=0):
        """
        Adds a person along with his/her balance to the database
        """
        models.TablePerson.insert(
            name=person_name, balance=initial_balance).execute()
        person = Person(person_name, initial_balance)
        self.people.update({person_name: person})
        return person

    def view_portfolio(self):
        """
        View list of stocks owned, their quantities and value
        """
        pass

    def get_transaction_history(self):
        """
        Get list of transactions made from log file
        """
        return self.log

    def logger(self, user, action, symbol, cost=0, quantity=0, amount=0, new_balance):
        """
        Logs all actions performed: BUY, SELL, ADD_FUNDS
        Format:
        Date | User | Action | Symbol | Cost | Quantity | Amount | Balance
        """
        if cost != 0 and quantity != 0:
            amount = cost * quantity
        else:
            cost = 0
            quantity = 0
            if amount <= 0:
                return

        transaction = pandas.DataFrame({'Name': user,
                                        'Action': action,
                                        'Symbol': symbol,
                                        'Cost': cost,
                                        'Quantity': quantity,
                                        'Amount': cost * quantity,
                                        'Balance': new_balance
                                        },
                                       index=[pandas.Timestamp('now')])
        self.log.append(transaction)
        return
