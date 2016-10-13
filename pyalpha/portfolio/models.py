import peewee

db = peewee.SqliteDatabase("portfolio.db")


class TableStock(peewee.Model):
    """
    Database Table containing list of stocks held
    """
    stock = peewee.CharField()

    class Meta:
        database = db


class TablePortfolio(peewee.Model):
    """
    Database Table containing:
        - Stocks held
        - Their Purchase price
        - Quantity Held
    """
    stock = peewee.ForeignKeyField(TableStock)
    purchase_price = peewee.IntegerField()
    quantity = peewee.IntegerField()

    class Meta:
        database = db


def setup_portfolio_database():
    """
    Create database tables if required
    """
    try:
        TableStock.create_table()
    except peewee.OperationalError:
        print("Stock table already exists!")

    try:
        TablePortfolio.create_table()
    except peewee.OperationalError:
        print("Portfolio table already exists!")
