{% set is_open_source = cookiecutter.open_source_license != 'Not open source' -%}
{% for _ in cookiecutter.project_name %}={% endfor %}
{{ cookiecutter.project_name }}
{% for _ in cookiecutter.project_name %}={% endfor %}

{% if is_open_source %}
.. image:: https://img.shields.io/pypi/v/{{ cookiecutter.project_slug }}.svg
        :target: https://pypi.python.org/pypi/{{ cookiecutter.project_slug }}
        :alt: PyPI

.. image:: https://coveralls.io/repos/github/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/badge.svg?branch=master
        :target: https://coveralls.io/github/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}?branch=master
        :alt: Coverage Status

.. image:: https://readthedocs.org/projects/{{ cookiecutter.project_slug | replace("_", "-") }}/badge/?version=latest
        :target: https://{{ cookiecutter.project_slug | replace("_", "-") }}.readthedocs.io/en/latest/?version=latest
        :alt: Documentation Status
{%- endif %}

{{ cookiecutter.project_short_description }}

{% if is_open_source %}
* Documentation: https://{{ cookiecutter.project_slug | replace("_", "-") }}.readthedocs.io.


Installation
------------

.. code:: bash

    pip install {{ cookiecutter.project_slug }}

{% endif %}


How to Use
----------
- TODO


Contributing
------------
Contributions are welcome, feel free to open an Issue or Pull Request.

Pull requests must be for the `develop` branch.

.. code:: bash

    git clone https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}
    cd {{ cookiecutter.project_slug }}
    git checkout develop
    python -m venv .venv
    pip install -r requirements_dev.txt
    pre-commit install
    pytest
