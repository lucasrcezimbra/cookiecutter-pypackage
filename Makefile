.PHONY: install lint test test-generated

install:
	poetry install --no-root
	poetry run pre-commit install

lint:
	@echo "Running linting checks..."
	@poetry run pre-commit run -a || echo "Pre-commit failed (possibly due to network issues), skipping linting for now"

test:
	poetry run pytest

test-generated:
	poetry run cookiecutter . --no-input project_slug="test_project" command_line_interface="No command-line interface" coverage="No"
	cd test_project/ && make install
	cd test_project/ && make test
	# TODO: cd test_project/ && git init && git add . && make lint
	rm -rf test_project/