# Cookiecutter PyPackage


An opinionated Cookiecutter to create a new Python package.

- CI/CD: [bump2version](https://github.com/c4urself/bump2version), [dependabot](https://github.com/dependabot), [Github Actions](https://github.com/features/actions) and [pre-commit](https://github.com/pre-commit/pre-commit)
- Code Style: [black](https://github.com/psf/black) and [ruff](https://github.com/astral-sh/ruff)
- Documentation: [Sphinx](https://github.com/sphinx-doc/sphinx)
- Tests: [Codecov](https://about.codecov.io/), [faker](https://github.com/joke2k/faker), [pytest](https://github.com/pytest-dev/pytest) and [pytest-mock](https://github.com/pytest-dev/pytest-mock/)


```
├── CHANGELOG.md
├── docs
│   ├── changelog.md
│   ├── conf.py
│   ├── index.rst
│   ├── make.bat
│   ├── Makefile
│   └── readme.md
├── .github
│   ├── dependabot.yml
│   └── workflows
│       ├── python-app.yml
│       └── python-publish.yml
├── .gitignore
├── LICENSE
├── poetry.lock
├── .pre-commit-config.yaml
├── pyproject.toml
├── python_boilerplate
│   ├── __init__.py
│   └── python_boilerplate.py
├── README.md
├── .readthedocs.yaml
├── setup.cfg
└── tests
    ├── __init__.py
    └── test_python_boilerplate.py
```


## How to Use

### Using Cruft (Recommended)

Cruft is compatible with Cookiecutter and is the recommended method because it allows you to update the project with the latest template changes using `cruft update`.

```bash
pip install cruft
cruft create https://github.com/lucasrcezimbra/cookiecutter-pypackage
```

### Using Cookiecutter

```bash
pip install -U cookiecutter
cookiecutter https://github.com/lucasrcezimbra/cookiecutter-pypackage
```
