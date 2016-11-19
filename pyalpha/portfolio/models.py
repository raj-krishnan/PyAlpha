import peewee
import datetime

db = peewee.SqliteDatabase("portfolio.db")


class BaseModel(peewee.Model):
    class Meta:
        database = db  # this model uses the "portfolio.db" database


class TableStockExchange(BaseModel):
    """
    Database Table containing names of people along with their balances.
    """
    name = peewee.CharField(null=False)
    balance = peewee.FloatField()


class TableUserPortfolio(BaseModel):
    """
    Database Table containing:

        - ForeignKey as TableStockExchange
        - Stocks held
        - Their Average price
        - Quantity Held

    """
    person = peewee.ForeignKeyField(
        TableStockExchange, related_name='portfolio')
    stock = peewee.CharField(null=False)
    average_price = peewee.FloatField()
    quantity = peewee.IntegerField()


class TableLogger(BaseModel):
    """
    Database Table containing:
        
        - ForeignKey as TableStockExchange
        - Stocks
        - Their Purchase/ Selling price
        - Quantity of stocks in the transaction
        - Total quantity of the stock left after the transaction
        - Total investment in the stock left after the transaction
        - Balance left after the transaction
        - Transaction type (buy ar sell)
        - Timestamp of the transaction

    """
    person = peewee.ForeignKeyField(TableStockExchange, related_name='logger')
    stock = peewee.CharField(null=False)
    price = peewee.FloatField()
    quantity = peewee.IntegerField()
    total_quantity = peewee.IntegerField()
    total_value = peewee.FloatField()
    balance = peewee.FloatField()
    buy_or_sell = peewee.CharField(choices = [('buy','buy'),('sell','sell')])
    timestamp = peewee.DateTimeField(default=datetime.datetime.now)


def setup_portfolio_database():
    """
    Create database tables if required
    """
    try:
        TableStockExchange.create_table()
    except peewee.OperationalError:
        print("Stock Exchange table already exists!")

    try:
        TableUserPortfolio.create_table()
    except peewee.OperationalError:
        print("User Portfolio table already exists!")

    try:
        TableLogger.create_table()
    except peewee.OperationalError:
        print("Logger table already exists!")
