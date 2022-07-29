# Cookiecutter PyPackage


An opinionated Cookiecutter to create a new Python package.

- CI/CD: [bump2version](https://github.com/c4urself/bump2version), [dependabot](https://github.com/dependabot), [Github Actions](https://github.com/features/actions) and [pre-commit](https://github.com/pre-commit/pre-commit)
- Code Style: [flake8](https://github.com/PyCQA/flake8) and [isort](https://github.com/timothycrosley/isort)
- Documentation: [Sphinx](https://github.com/sphinx-doc/sphinx)
- Tests: [Coveralls](https://coveralls.io/), [faker](https://github.com/joke2k/faker), [pytest](https://github.com/pytest-dev/pytest) and [pytest-mock](https://github.com/pytest-dev/pytest-mock/)


```
├── CHANGELOG.rst
├── docs
│   ├── changelog.rst
│   ├── conf.py
│   ├── index.rst
│   ├── make.bat
│   ├── Makefile
│   ├── readme.rst
│   └── usage.rst
├── .github
│   ├── dependabot.yml
│   └── workflows
│       └── python-app.yml
├── .gitignore
├── LICENSE
├── MANIFEST.in
├── .pre-commit-config.yaml
├── python_boilerplate
│   ├── __init__.py
│   └── python_boilerplate.py
├── README.rst
├── requirements_dev.txt
├── setup.cfg
├── setup.py
├── tests
│   ├── __init__.py
│   └── test_python_boilerplate.py
└── tox.ini
```


## How to Use

```bash
pip install -U cookiecutter
cookiecutter https://github.com/lucasrcezimbra/cookiecutter-pypackage
```

## TODO

- [] Add Action to upload to PyPI
