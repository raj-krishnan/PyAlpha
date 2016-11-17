import datetime
import pandas

from pyalpha.portfolio import models
from pyalpha.data_structures.stock import Stock


class InputError(Exception):
    """
    Exception raised for errors in the input.

    Attributes
    ----------
    expression : input expression in which the error occurred
    message : explanation of the error
    """

    def __init__(self, expression, message):
        self.expression = expression
        self.message = message


class UserPortfolio:
    """
    A UserPortfolio object will provide access to handle the portfolio of a
    single person

    Parameters
    ----------
    person_name : string
        Name of the person.
    initial_balance : float or int
        Initial balance in the person's portfolio

    Attributes
    ----------
    name : string
        name of the person
    balance : float or int
        balance in hand

    Methods
    -------
    * add_funds(self, deposit)
    * buy_stock(self, symbol, quantity)
    * sell_stock(self, symbol, quantity)
    * view_portfolio(self)
    """

    def __init__(self, person_name, initial_balance):
        self.name = person_name
        self.balance = initial_balance

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

    def _get_stock_quote(self, symbol):
        """
        Get the current price of a stock
        """
        stock = Stock(symbol)
        stock.fetch_price()
        return stock.price

    def _logger(self, person_record,
                symbol, stock_price, quantity, buy_or_sell,
                total_stock_quantity, total_stock_value, balance):
        """
        - Logs transactions made by the user in the Logger Table
        """
        new_logger_record = models.TableLogger(
            person=person_record, stock=symbol,
            price=stock_price, quantity=quantity, buy_or_sell=buy_or_sell,
            total_quantity=total_stock_quantity, total_value=total_stock_value,
            balance=balance, timestamp=datetime.datetime.now())
        new_logger_record.save()
        return True

    def buy_stock(self, symbol, quantity):
        """
        - Buy the given 'quantity' of stock specified by 'symbol'
        - Returns True if the transaction is successful and False otherwise
        """
        if type(quantity) != int or quantity < 0:
            err = InputError(
                quantity, ', which is the amount of stock to be purchased \
can only be a positive integer')
            print(err.expression, err.message)
            return False

        stock_price = self._get_stock_quote(symbol)
        if stock_price * quantity > self.balance:
            # Insufficient Funds
            err = InputError(
                quantity, 'stocks cannot be bought due to insufficient funds')
            print(err.expression, err.message)
            return False
        person_record = models.TableStockExchange.get(
            models.TableStockExchange.name == self.name)
        portfolio_record = (
            models.TableUserPortfolio
            .select()
            .where(models.TableUserPortfolio.person == person_record,
                   models.TableUserPortfolio.stock == symbol))

        if portfolio_record.exists():
            portfolio_record = portfolio_record.get()
            new_average = (
                portfolio_record.average_price * portfolio_record.quantity +
                stock_price * quantity) / (portfolio_record.quantity + quantity
                                           )
            # Modify entry in TablePortfolio
            portfolio_record.average_price = new_average
            portfolio_record.quantity += quantity
            portfolio_record.save()
            total_stock_quantity = portfolio_record.quantity
            total_stock_value = new_average * total_stock_quantity
        else:
            new_average = stock_price
            # Add entry to TablePortfolio
            new_portfolio_record = models.TableUserPortfolio(
                person=person_record, stock=symbol,
                average_price=new_average, quantity=quantity)
            new_portfolio_record.save()
            total_stock_quantity = quantity
            total_stock_value = new_average * total_stock_quantity

        # Update the balance of the person
        self.balance = self.balance - stock_price * quantity
        # Modify entry in TablePerson
        person_record.balance = self.balance
        person_record.save()

        # Add the transaction to the logger
        self._logger(person_record, symbol, stock_price, quantity, 'buy',
                     total_stock_quantity, total_stock_value, self.balance)
        # Transaction successful !!!
        return True

    def sell_stock(self, symbol, quantity):
        """
        - Sell the given 'quantity' of stock specified by 'symbol'
        - Returns True if the transaction is successful and False otherwise
        """
        if type(quantity) != int or quantity < 0:
            err = InputError(
                quantity, ', which is the amount of stock to be sold \
can only be a positive integer')
            print(err.expression, err.message)
            return False

        stock_price = self._get_stock_quote(symbol)
        person_record = models.TableStockExchange.get(
            models.TableStockExchange.name == self.name)
        portfolio_record = (
            models.TableUserPortfolio
            .select()
            .where(models.TableUserPortfolio.person == person_record,
                   models.TableUserPortfolio.stock == symbol))
        if portfolio_record.exists():
            portfolio_record = portfolio_record.get()
            if quantity < portfolio_record.quantity:
                new_average = (
                    portfolio_record.average_price *
                    portfolio_record.quantity -
                    stock_price * quantity) / (portfolio_record.quantity -
                                               quantity)
                # Modify entry in TablePortfolio
                portfolio_record.average_price = new_average
                portfolio_record.quantity -= quantity
                portfolio_record.save()
                total_stock_quantity = portfolio_record.quantity
                total_stock_value = new_average * total_stock_quantity
            elif quantity == portfolio_record.quantity:
                # All the holdings of a stock are sold
                portfolio_record.delete_instance()
                total_stock_quantity = 0
                total_stock_value = 0
            else:
                # The amount to sell is more than what the person holds
                err = InputError(
                    quantity, ', stocks are not available to sell')
                print(err.expression, err.message)
                return False
        else:
            # The specified stock doesn't exist
            err = InputError(
                symbol, 'does not exist in the user\'s portfolio')
            print(err.expression, err.message)
            return False

        # Update the balance of the person
        self.balance = self.balance + stock_price * quantity
        # Modify entry in TablePerson
        person_record.balance = self.balance
        person_record.save()

        # Add the transaction to the logger
        self._logger(person_record, symbol, stock_price, quantity, 'sell',
                     total_stock_quantity, total_stock_value, self.balance)
        # Transaction successful !!!
        return True

    def view_portfolio(self):
        """
        - View list of stocks owned, their quantities and value
        - Returns pandas.DataFrame object which can be printed to view
          the portfolio of the person
        """
        person_record = models.TableStockExchange.get(
            models.TableStockExchange.name == self.name)
        portfolio_record = (
            models.TableUserPortfolio
            .select()
            .where(models.TableUserPortfolio.person == person_record))
        records = pandas.DataFrame()
        for i, record in enumerate(portfolio_record, 1):
            record_df = pandas.DataFrame(
                                {'Stock': record.stock,
                                 'Average Price': record.average_price,
                                 'Quantity': record.quantity,
                                 },
                                index=[i])
            records = records.append(record_df)
        return records

    def view_log(self, symbol=None,
                 start_date=datetime.date.min,
                 end_date=datetime.datetime.now().date(),
                 start_time=datetime.time.min,
                 end_time=datetime.time.max):
        """
        - View the log
        """""
        person_record = models.TableStockExchange.get(
            models.TableStockExchange.name == self.name)
        if symbol is None:
            logger_record = (
                models.TableLogger
                .select()
                .where((models.TableLogger.person == person_record) &
                       (models.TableLogger.timestamp <
                        datetime.datetime.combine(end_date, end_time)) &
                       (models.TableLogger.timestamp >
                        datetime.datetime.combine(start_date, start_time))))
        else:
            logger_record = (
                models.TableLogger
                .select()
                .where((models.TableLogger.person == person_record) &
                       (models.TableLogger.stock == symbol) &
                       (models.TableLogger.timestamp <
                        datetime.datetime.combine(end_date, end_time)) &
                       (models.TableLogger.timestamp >
                        datetime.datetime.combine(start_date, start_time))))

        # Returning the table with log details
        records = pandas.DataFrame()
        for i, record in enumerate(logger_record, 1):
            record_df = pandas.DataFrame(
                    {'Stock': record.stock,
                     'Transaction Stock Price': record.price,
                     'Transaction Stock Quantity': record.quantity,
                     'Stock Quantity after Transaction': record.total_quantity,
                     'Stock Value after Transaction': record.total_value,
                     'Balance after Transaction': record.balance,
                     'Transaction type': record.buy_or_sell,
                     'The timestamp of the Transaction': record.timestamp
                     },
                    index=[i]
                                         )
            records = records.append(record_df)
        return records


class StockExchange:
    """
    A StockExchange object handles the database containing portfolio details
    of users.

    Attributes
    ----------
    users : dictionary
        Contains 'name of the person' as the key, with
        corresponding'Person object' as the value

    Methods
    -------
    * add_user(self, person_name, initial_balance)
    """

    def __init__(self):
        models.setup_portfolio_database()
        self.users = {}

    def add_user(self, person_name="", initial_balance=0):
        """
        Adds an user along with his/her balance to the database
        """
        if initial_balance < 0:
            err = InputError(
                initial_balance, ', which is the initial balance \
available to the user should be positive')
            print(err.expression, err.message)
            return
        models.TableStockExchange.insert(
            name=person_name, balance=initial_balance).execute()
        person = UserPortfolio(person_name, initial_balance)
        self.users.update({person_name: person})
        return person

    def view_log(self, symbol=None,
                 start_date=datetime.date.min,
                 end_date=datetime.datetime.now().date(),
                 start_time=datetime.time.min,
                 end_time=datetime.time.max):
        """
        - View Stock Exchange log
        """
        if symbol is None:
            logger_record = (
                models.TableLogger
                .select(models.TableLogger.stock,
                        models.TableLogger.price,
                        models.TableLogger.quantity,
                        models.TableLogger.buy_or_sell,
                        models.TableLogger.timestamp)
                .where((models.TableLogger.timestamp <
                        datetime.datetime.combine(end_date, end_time)) &
                       (models.TableLogger.timestamp >
                        datetime.datetime.combine(start_date, start_time))))
        else:
            logger_record = (
                models.TableLogger
                .select(models.TableLogger.stock,
                        models.TableLogger.price,
                        models.TableLogger.quantity,
                        models.TableLogger.buy_or_cell,
                        models.TableLogger.timestamp)
                .where((models.TableLogger.stock == symbol) &
                       (models.TableLogger.timestamp <
                        datetime.datetime.combine(end_date, end_time)) &
                       (models.TableLogger.timestamp >
                        datetime.datetime.combine(start_date, start_time))))

        # Returning the table with log details
        records = pandas.DataFrame()
        for i, record in enumerate(logger_record, 1):
            record_df = pandas.DataFrame(
                    {'Stock': record.stock,
                     'Transaction Stock Price': record.price,
                     'Transaction Stock Quantity': record.quantity,
                     'Transaction type': record.buy_or_sell,
                     'The timestamp of the Transaction': record.timestamp
                     },
                    index=[i]
                                         )
            records = records.append(record_df)
        return records
