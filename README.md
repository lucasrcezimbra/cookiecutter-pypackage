# Cookiecutter PyPackage


An opinionated Cookiecutter to create a new Python package.

- CI/CD: [bump2version](https://github.com/c4urself/bump2version), [dependabot](https://github.com/dependabot), [Github Actions](https://github.com/features/actions) and [pre-commit](https://github.com/pre-commit/pre-commit)
- Code Style: [black](https://github.com/psf/black) and [ruff](https://github.com/astral-sh/ruff)
- Documentation: [Sphinx](https://github.com/sphinx-doc/sphinx)
- Tests: [Codecov](https://about.codecov.io/), [faker](https://github.com/joke2k/faker), [pytest](https://github.com/pytest-dev/pytest) and [pytest-mock](https://github.com/pytest-dev/pytest-mock/)
- Template Management: [cruft](https://github.com/cruft/cruft) for keeping projects up-to-date with template changes


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

### Using Cookiecutter (Standard Method)

```bash
pipx install cookiecutter
cookiecutter https://github.com/lucasrcezimbra/cookiecutter-pypackage
```

### Using Cruft (Recommended for Template Updates)

[Cruft](https://github.com/cruft/cruft) allows you to keep your project up-to-date with template changes:

```bash
pipx install cruft
cruft create https://github.com/lucasrcezimbra/cookiecutter-pypackage
```

Later, to update your project when the template changes:

```bash
cd your-project
cruft update
```

To check if your project is up-to-date:

```bash
cruft check
```

To see what would change:

```bash
cruft diff
```
