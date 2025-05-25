"""Console script for {{cookiecutter.namespace}}."""

{%- if cookiecutter.command_line_interface|lower == 'argparse' %}
import argparse
{%- endif %}
import sys
{%- if cookiecutter.command_line_interface|lower == 'click' %}
import click
{%- endif %}
{%- if cookiecutter.command_line_interface|lower == 'typer' %}
import typer
{%- endif %}

{% if cookiecutter.command_line_interface|lower == 'click' %}
@click.command()
def main(args=None):
    """Console script for {{cookiecutter.namespace}}."""
    click.echo("Replace this message by putting your code into "
               "{{cookiecutter.namespace}}.cli.main")
    click.echo("See click documentation at https://click.palletsprojects.com/")
    return 0
{%- endif %}
{%- if cookiecutter.command_line_interface|lower == 'argparse' %}
def main():
    """Console script for {{cookiecutter.namespace}}."""
    parser = argparse.ArgumentParser()
    parser.add_argument('_', nargs='*')
    args = parser.parse_args()

    print("Arguments: " + str(args._))
    print("Replace this message by putting your code into "
          "{{cookiecutter.namespace}}.cli.main")
    return 0
{%- endif %}
{%- if cookiecutter.command_line_interface|lower == 'typer' %}
app = typer.Typer()

@app.command()
def main():
    """Console script for {{cookiecutter.namespace}}."""
    typer.echo("Replace this message by putting your code into "
               "{{cookiecutter.namespace}}.cli.main")
    typer.echo("See typer documentation at https://typer.tiangolo.com/")
    return 0
{%- endif %}


if __name__ == "__main__":
{%- if cookiecutter.command_line_interface|lower == 'typer' %}
    app()  # pragma: no cover
{%- else %}
    sys.exit(main())  # pragma: no cover
{%- endif %}
