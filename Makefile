PIP = pip3
PYTHON = python3

.PHONY: all requirements clean coverage docs tests help

all: requirements
	$(PYTHON) setup.py install --user

requirements:
	$(PIP) install --user -r requirements.txt

clean:
	rm -rf build/
	rm -rf dist/
	rm -rf __pycache__/
	rm -f .coverage
	rm -rf htmlcov/
	rm -rf PyAlpha.egg-info

coverage:
	coverage run -m nose.core
	coverage report -m
	coverage html

docs:
	cd docs/ && make clean
	cd docs/ && make html

tests:
	nosetests -v

help:
	@echo 'run "make" or "make all" to install the module'
	@echo 'run "make clean" to clean build and coverage files'
	@echo 'run "make coverage" to generage coverage'
	@echo 'run "make docs" to generate documentation using sphinx'
	@echo 'run "make tests" to run all the tests'
