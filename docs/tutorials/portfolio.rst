=================================
Tutorial: User Portfolio Handling
=================================

This tutorial gives a basic example of how PyAlpha can be used to handle user
porfolios.

First, import the following module:

.. code-block:: python

    from pyalpha.portfolio.portfolio import StockExchange

Now, create an exchange portal where trading is done and add an user with an
initial balance of 10000:

.. code-block:: python
    
    stock_exchange = StockExchange()
    John = stock_exchange.add_user('John', 10000)

The user can now buy or sell stocks:

.. code-block:: python
    
    John.buy_stock('AAPL', 3)
    John.buy_stock('GOOGL', 5)
    John.sell_stock('AAPL', 2)

Adding another user to the exchange:

.. code-block:: python

    Emma = stock_exchange.add_user('Emma', 20000)
    Emma.buy_stock('TSLA', 6)

An user's portfolio can be viewed as:

.. code-block:: python

    portfolio_John = John.view_portfolio() # returns a pandas.DataFrame object
    print(portfolio_John)

And finally logs of both the user's portfolio and stock exchange can be
viewed as:

.. sourcecode:: python

    >>> John.view_log()
    >>> Emma.view_log("TSLA") # view the transaction log of a specific stock
    >>> stock_exchange.view_log()
