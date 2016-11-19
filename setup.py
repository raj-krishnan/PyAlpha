from distutils.core import setup

requires = ["numpy",
            "pandas",
            "peewee",
            "ystockquote"]

setup(name='PyAlpha',
      version='0.1',
      description='Alpha Testing Utility',
      author='Raj Krishnan',
      author_email='rajkrishnan1996@gmail.com',
      license='BSD',
      install_requires=requires,
      packages=['pyalpha',
                'pyalpha.alpha',
                'pyalpha.data_structures',
                'pyalpha.portfolio'],
      )
