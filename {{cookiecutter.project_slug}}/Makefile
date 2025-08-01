.PHONY: build lint run test{% if cookiecutter.coverage == "Codecov" %} test-cov{% endif %} update-template

build:
	poetry run python -m build

install:
	poetry install
	poetry run pre-commit install

lint:
	poetry run pre-commit run -a

test:
	poetry run pytest
{% if cookiecutter.coverage == "Codecov" %}

test-cov:
	 poetry run pytest --cov={{cookiecutter.namespace}}
{% endif %}

update-template:
	cruft update
