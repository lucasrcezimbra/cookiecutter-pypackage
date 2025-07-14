{% set is_open_source = cookiecutter.open_source_license != 'Not open source' -%}
# {{ cookiecutter.project_name }}

{% if is_open_source %}
[![PyPI](https://img.shields.io/pypi/v/{{ cookiecutter.project_slug }}.svg)](https://pypi.python.org/pypi/{{ cookiecutter.project_slug }})
{% if cookiecutter.coverage == "Codecov" %}
[![codecov](https://codecov.io/gh/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/graph/badge.svg)](https://codecov.io/gh/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }})
{% endif %}
[![Documentation Status](https://readthedocs.org/projects/{{ cookiecutter.project_slug }}/badge/?version=latest)](https://{{ cookiecutter.project_slug | replace("_", "-") }}.readthedocs.io/en/latest/?version=latest)
{%- endif %}

{{ cookiecutter.project_short_description }}

{% if is_open_source %}
* Documentation: https://{{ cookiecutter.project_slug }}.readthedocs.io.


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
make install
make test
```

## Template Updates

This project was created using [cookiecutter-pypackage](https://github.com/lucasrcezimbra/cookiecutter-pypackage). 
To keep the project structure up-to-date with template changes, use [cruft](https://github.com/cruft/cruft):

```bash
# Check if the project is up-to-date with the template
cruft check

# Show differences between current project and latest template
cruft diff

# Update the project with latest template changes
cruft update
```
