=======
PyAlpha
=======

|Build_Status| |Coverage| |Documentation|

PyAlpha is a python toolbox for backtesting trading ideas. An Alpha is a 
concrete trading idea that can be simulated historically.


In PyAlpha, an 'Alpha' refers to a mathematical model or strategy, written as 
python code, which places different bets (weights) on different stocks, and is
expected to be profitable in the long run.

Dependencies
------------

- peewee
- pandas
- ystockquote

Installation
------------

.. sourcecode:: bash

    $ git clone https://github.com/raj-krishnan/PyAlpha.git
    $ cd PyAlpha
    $ pip install -r requirements.txt
    $ python setup.py install

.. |Build_Status| image:: https://travis-ci.org/raj-krishnan/PyAlpha.svg?branch=master
   :target: https://travis-ci.org/raj-krishnan/PyAlpha

.. |Coverage| image:: https://coveralls.io/repos/github/raj-krishnan/PyAlpha/badge.svg?branch=master
   :target: https://coveralls.io/github/raj-krishnan/PyAlpha?branch=master

.. |Documentation| image:: http://readthedocs.org/projects/pyalpha/badge/?version=latest
   :target: http://pyalpha.readthedocs.io/en/latest/?badge=latest
   :alt: Documentation Status
