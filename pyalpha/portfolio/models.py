import peewee

db = peewee.SqliteDatabase("portfolio.db")


class BaseModel(peewee.Model):
    class Meta:
        database = db  # this model uses the "portfolio.db" database


class TablePerson(BaseModel):
    """
    Database Table containing names of people
    """
    name = peewee.CharField(null=False)


class TablePortfolio(BaseModel):
    """
    Database Table containing:
        - Stocks held
        - Their Purchase price
        - Quantity Held
    """
    person = peewee.ForeignKeyField(TablePerson, related_name='portfolio')
    stock = peewee.CharField()
    purchase_price = peewee.IntegerField()
    quantity = peewee.IntegerField()


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
