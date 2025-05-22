.PHONY: test lint ci

install:
	pip install -r requirements-test.txt

test:
	pytest -v --cov-report=html

lint:
	flake8 core

ci: lint test

run-example:
	PYTHONPATH=. python examples/basic_usage.py

clean:
	find . -name "*.pyc" -delete
	find . -name "__pycache__" -delete
	rm -rf .coverage htmlcov