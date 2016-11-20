PIP = pip3
PYTHON = python3

.PHONY: all requirements clean docs tests

all: requirements
	$(PYTHON) setup.py install --user

requirements:
	$(PIP) install --user -r requirements.txt

clean:
	rm -rf build/
	rm -rf __pycache__/

docs:
	cd docs/ && make clean
	cd docs/ && make html

tests:
	nosetests -v

