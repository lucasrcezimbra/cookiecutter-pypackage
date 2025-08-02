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
	cd python_boilerplate/ && make install
	cd python_boilerplate/ && make test
	cd python_boilerplate/ && git init && git add . && make lint
	rm -rf python_boilerplate/
