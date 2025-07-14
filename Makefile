.PHONY: install lint test test-generated

install:
	poetry install --no-root
	poetry run pre-commit install
	poetry run pre-commit install-hooks

lint:
	poetry run pre-commit run -a

test:
	poetry run pytest
