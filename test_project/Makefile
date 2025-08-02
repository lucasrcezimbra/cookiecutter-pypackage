.PHONY: build lint run test test-cov

build:
	poetry run python -m build

install:
	poetry install
	poetry run pre-commit install
	poetry run pre-commit install-hooks

lint:
	poetry run pre-commit run -a

test:
	poetry run pytest


test-cov:
	 poetry run pytest --cov=test_project

