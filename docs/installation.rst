============
Installation
============

**Note: Python 3 is required**

------------
Dependencies
------------

 - Numpy
 - ystockquote
 - pandas
 - peewee

-------------
Linux and OSX
-------------

To install PyAlpha, clone this repository by::

    $ git clone https://github.com/raj-krishnan/PyAlpha

To install dependencies, run::

    $ pip install -r requirements.txt

To install, run::

    $ python setup.py install

**PyAlpha doesn't support Windows currently**

-----------------
Running the tests
-----------------

For running the tests you will need to install ``nose``, install using::

    $ pip install nose

To run the tests, from project's root directory run::

    $ nosetests -v

