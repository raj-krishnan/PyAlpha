import pandas

from pyalpha.portfolio import models
from pyalpha.data_structures.Stock import Stock


class Error(Exception):
    """Base class for exceptions in this module."""
    pass


class InputError(Error):
    """
    Exception raised for errors in the input.
    Attributes:
        expression -- input expression in which the error occurred
        message -- explanation of the error
    """

    def __init__(self, expression, message):
        self.expression = expression
        self.message = message


class Person():
    """
    Object with
    """

    def __init__(self, person_name, initial_balance, log):
        self.name = person_name
        self.balance = initial_balance
        self.log = log

    def add_funds(self, deposit):
        """
        Increase balance in the account
        """
        if deposit < 0:
            err = InputError(
                deposit, ', which is the amount to be deposited is positive')
            print(err.expression, err.message)
            return

        self.balance += deposit

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
        if type(quantity) != int or quantity < 0:
            err = InputError(
                quantity, ', which is the amount of stock to be purchased can only be a positive integer')
            print(err.expression, err.message)
            return False

        stock_price = self.get_stock_quote(symbol)
        if stock_price * quantity > self.balance:
            # Insufficient Funds
            return False
        person_record = models.TablePerson.get(
            models.TablePerson.name == self.name)
        portfolio_record = (models.TablePortfolio
                            .select()
                            .where(models.TablePortfolio.person == person_record,
                                   models.TablePortfolio.stock == symbol))

        if portfolio_record.exists():
            portfolio_record = portfolio_record.get()
            new_average = (portfolio_record.average_price * portfolio_record.quantity +
                           stock_price * quantity) / (portfolio_record.quantity + quantity)
            # Modify entry in TablePortfolio
            portfolio_record.average_price = new_average
            portfolio_record.quantity += quantity
            portfolio_record.save()
        else:
            new_average = stock_price
            # Add entry to TablePortfolio
            new_portfolio_record = models.TablePortfolio(
                person=person_record, stock=symbol,
                average_price=new_average, quantity=quantity)
            new_portfolio_record.save()

        # Update the balance of the person
        self.balance = self.balance - stock_price * quantity

        # Modify entry in TablePerson
        person_record.balance = self.balance
        person_record.save()
        # Transaction successful !!!
        return True

    def sell_stock(self, symbol, quantity):
        """
        Sell the specified amount of a stock
        """
        if type(quantity) != int or quantity < 0:
            err = InputError(
                quantity, ', which is the amount of stock to be sold can only be a positive integer')
            print(err.expression, err.message)
            return False

        stock_price = self.get_stock_quote(symbol)
        person_record = models.TablePerson.get(
            models.TablePerson.name == self.name)
        portfolio_record = (models.TablePortfolio
                            .select()
                            .where(models.TablePortfolio.person == person_record,
                                   models.TablePortfolio.stock == symbol))
        if portfolio_record.exists():
            portfolio_record = portfolio_record.get()
            if quantity < portfolio_record.quantity:
                new_average = (portfolio_record.average_price * portfolio_record.quantity -
                               stock_price * quantity) / (portfolio_record.quantity - quantity)
                # Modify entry in TablePortfolio
                portfolio_record.average_price = new_average
                portfolio_record.quantity -= quantity
                portfolio_record.save()
            elif quantity == portfolio_record.quantity:
                # All the holdings of a stock are sold
                portfolio_record.delete_instance()
            else:
                # The amount to sell is more than what the person holds
                return False
        else:
            # The specified stock doesn't exist
            return False

        # Update the balance of the person
        self.balance = self.balance + stock_price * quantity
        # Modify entry in TablePerson
        person_record.balance = self.balance
        person_record.save()
        return True

    def view_portfolio(self):
        """
        View list of stocks owned, their quantities and value
        """
        person_record = models.TablePerson.get(
            models.TablePerson.name == self.name)
        portfolio_record = (models.TablePortfolio
                            .select()
                            .where(models.TablePortfolio.person == person_record))
        records = pandas.DataFrame()
        for record in portfolio_record:
            record_df = pandas.DataFrame({'Stock': record.stock,
                                          'Average Price': record.average_price,
                                          'Quantity': record.quantity,
                                          },
                                         index=[pandas.Timestamp('now')])
            records = records.append(record_df)
        return records
        # print('The portfolio details of %s:' % (self.name))
        # print(['Stock', 'Average Price', 'Quantity'])
        #     print([record.stock, record.average_price, record.quantity])

        # def get_transaction_history(self, user=""):
        #     """
        #     Get list of transactions made from log file
        #     """
        #     return self.log.loc[self.log['Name'] == user]


class Portfolio:
    def __init__(self):
        models.setup_portfolio_database()
        # Contains 'name of the person' as the key, with the 'Person object' as
        # the value
        self.person = {}
        self.log = pandas.DataFrame()

    def add_person(self, person_name="", initial_balance=0):
        """
        Adds a person along with his/her balance to the database
        """
        if initial_balance < 0:
            err = InputError(
                initial_balance, ', which is the initial balance available to a person is positive')
            print(err.expression, err.message)
            return
        models.TablePerson.insert(
            name=person_name, balance=initial_balance).execute()
        person = Person(person_name, initial_balance, self.log)
        self.person.update({person_name: person})
        return person

    # def get_transaction_history(self):
    #     """
    #     Get list of transactions made from log file
    #     """
    #     return self.log
    #
    # def logger(self, user, action, symbol, new_balance, cost=0, quantity=0, amount=0):
    #     """
    #     Logs all actions performed: BUY, SELL, ADD_FUNDS
    #     Format:
    #     Date | User | Action | Symbol | Cost | Quantity | Amount | Balance
    #     """
    #     if cost != 0 and quantity != 0:
    #         amount = cost * quantity
    #     else:
    #         cost = 0
    #         quantity = 0
    #         if amount <= 0:
    #             return
    #
    #     transaction = pandas.DataFrame({'Name': user,
    #                                     'Action': action,
    #                                     'Symbol': symbol,
    #                                     'Cost': cost,
    #                                     'Quantity': quantity,
    #                                     'Amount': amount,
    #                                     'Balance': new_balance
    #                                     },
    #                                    index=[pandas.Timestamp('now')])
    #     self.log = self.log.append(transaction)
    #     return
