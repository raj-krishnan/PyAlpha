=======================
Tutorial: Alpha Testing
=======================

This tutorial guides you with building and testing your first alpha.

First, import the following modules:

.. code-block:: python

    from pyalpha.alpha.alpha import Alpha
    import pyalpha.alpha.stock_lists as stock_lists

Now, inherit the Alpha class and define your custom alpha. In this example, we
will use the alpha: 1/closing_price

.. code-block:: python

    class AlphaDataset(Alpha):
        def alpha(self, stock):
            return 1.0/stock.close

Now, setup the class using S&P100, fetch historical stock data and run the
simulation:

.. code-block:: python

    start_date = "2015-01-02"
    end_date = "2016-12-31"
    alpha = AlphaDataset(stock_lists.SNP100,
                         start_date,
                         end_date)
    alpha.construct_historical_data()
    alpha.simulate()

You now have the daily return (as a percentage) and the turnover stored here:

.. code-block:: python

    alpha.returns
    alpha.turnover

