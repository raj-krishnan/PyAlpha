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

-------------------
Installing with git
-------------------

This project is hosted at https://github.com/raj-krishnan/PyAlpha and can be installed using git:

.. sourcecode:: bash

    $ git clone https://github.com/raj-krishnan/PyAlpha.git
    $ cd PyAlpha

Install the dependencies using::

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

