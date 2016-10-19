import peewee

db = peewee.SqliteDatabase("portfolio.db")


class BaseModel(peewee.Model):
    class Meta:
        database = db  # this model uses the "portfolio.db" database


class TablePerson(BaseModel):
    """
    Database Table containing names of people along with their balances.
    """
    name = peewee.CharField(null=False)
    balance = peewee.FloatField()


class TablePortfolio(BaseModel):
    """
    Database Table containing:
        - Stocks held
        - Their Average price
        - Quantity Held
    """
    person = peewee.ForeignKeyField(TablePerson, related_name='portfolio')
    stock = peewee.CharField(null=False)
    average_price = peewee.FloatField()
    quantity = peewee.IntegerField()


class TableLogger(BaseModel):
    """
    Database Table containing:
        - Stocks
        - Their Purchase/ Selling price
        - Quantity of stocks in the transaction
        - Timestamp of the transaction
    """
    person = peewee.ForeignKeyField(TablePerson, related_name='logger')
    stock = peewee.CharField(null=False)
    transaction_price = peewee.FloatField()
    quantity = peewee.IntegerField()
    timestamp = peewee.DateTimeField()

# def before_request_handler():
#     database.connect()


# def after_request_handler():
#     database.close()


def setup_portfolio_database():
    """
    Create database tables if required
    """
    try:
        TablePerson.create_table()
    except peewee.OperationalError:
        print("People table already exists!")

    try:
        TablePortfolio.create_table()
    except peewee.OperationalError:
        print("Portfolio table already exists!")
