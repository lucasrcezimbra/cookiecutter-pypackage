.PHONY: install lint test test-generated

install:
	poetry install --no-root
	poetry run pre-commit install
	poetry run pre-commit install-hooks

lint:
	poetry run pre-commit run -a

test:
	poetry run pytest

test-generated:
	poetry run cookiecutter . --no-input
	cd python-boilerplate/ && make install
	cd python-boilerplate/ && make test
	cd python-boilerplate/ && git init && git add . && make lint
	rm -rf python-boilerplate/
