.PHONY: lint run test{% if cookiecutter.coverage == "Codecov" %} test-cov{% endif %}

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
