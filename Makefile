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
	poetry run cookiecutter . --no-input project_slug="test_project"
	cd test_project/ && make install
	cd test_project/ && make test
	cd test_project/ && git init && git add . && make lint
	rm -rf test_project/
