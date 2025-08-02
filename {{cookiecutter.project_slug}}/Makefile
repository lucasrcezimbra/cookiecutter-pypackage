.PHONY: build lint run test{% if cookiecutter.coverage == "Codecov" %} test-cov{% endif %} update-template

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
{% if cookiecutter.coverage == "Codecov" %}

test-cov:
	 poetry run pytest --cov={{cookiecutter.namespace}}
{% endif %}

update-template:
	poetry run cruft update
