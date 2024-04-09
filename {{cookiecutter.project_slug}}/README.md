{% set is_open_source = cookiecutter.open_source_license != 'Not open source' -%}
# {{ cookiecutter.project_name }}

{% if is_open_source %}
[![PyPI](https://img.shields.io/pypi/v/{{ cookiecutter.project_slug }}.svg)](https://pypi.python.org/pypi/{{ cookiecutter.project_slug }})
{% if cookiecutter.coverage == "Codecov" %}
[![codecov](https://codecov.io/gh/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/graph/badge.svg)](https://codecov.io/gh/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }})
{% endif %}
[![Documentation Status](https://readthedocs.org/projects/{{ cookiecutter.project_slug | replace("_", "-") }}/badge/?version=latest)](https://{{ cookiecutter.project_slug | replace("_", "-") }}.readthedocs.io/en/latest/?version=latest)
{%- endif %}

{{ cookiecutter.project_short_description }}

{% if is_open_source %}
* Documentation: https://{{ cookiecutter.project_slug | replace("_", "-") }}.readthedocs.io.


## Installation

```bash
pip install {{ cookiecutter.project_slug }}
```

{% endif %}


## How to Use

- TODO


## Contributing

Contributions are welcome, feel free to open an Issue or Pull Request.

```
git clone https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}
cd {{ cookiecutter.project_slug }}
python -m venv .venv
source .venv/bin/activate
pip install .[test]
pre-commit install
pytest
```
