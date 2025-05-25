import importlib
import os
import shlex
import subprocess
from contextlib import contextmanager
from textwrap import dedent

import pytest
from click.testing import CliRunner


@contextmanager
def inside_dir(dirpath):
    old_path = os.getcwd()
    try:
        os.chdir(dirpath)
        yield
    finally:
        os.chdir(old_path)


def run_inside_dir(command, dirpath):
    with inside_dir(dirpath):
        return subprocess.check_call(shlex.split(command))


def project_info(result):
    namespace = result.context["namespace"]
    project_dir = result.project_path / namespace
    return result.project_path, namespace, project_dir


def test_bake_with_defaults(cookies):
    result = cookies.bake()

    assert result.exit_code == 0
    assert result.exception is None

    found_toplevel_files = [f.name for f in result.project_path.iterdir()]
    assert "pyproject.toml" in found_toplevel_files
    assert "python_boilerplate" in found_toplevel_files
    assert "tests" in found_toplevel_files


def test_bake_selecting_license(cookies):
    license_strings = (
        (
            "GNU Lesser General Public License v2.1",
            "GNU LESSER GENERAL PUBLIC LICENSE",
            "License :: OSI Approved :: GNU Lesser General Public License v2 (LGPLv2)",
        ),
        (
            "MIT license",
            "MIT ",
            "License :: OSI Approved :: MIT License",
        ),
        (
            "GNU General Public License v3",
            "GNU GENERAL PUBLIC LICENSE",
            "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        ),
    )
    for license, target_string, classifier in license_strings:
        result = cookies.bake(extra_context={"open_source_license": license})
        assert target_string in (result.project_path / "LICENSE").read_text()
        assert classifier in (result.project_path / "pyproject.toml").read_text()


def test_bake_not_open_source(cookies):
    result = cookies.bake(extra_context={"open_source_license": "Not open source"})

    found_toplevel_files = [f.name for f in result.project_path.iterdir()]
    assert "LICENSE" not in found_toplevel_files
    assert "License" not in (result.project_path / "README.md").read_text()
    assert "License" not in (result.project_path / "pyproject.toml").read_text()


@pytest.mark.skip("TODO: fixme")
def test_using_pytest(cookies):
    result = cookies.bake()

    assert result.project.isdir()
    test_file_path = result.project.join("tests/test_python_boilerplate.py")
    lines = test_file_path.readlines()
    assert "def test_python_boilerplate():" in "".join(lines)
    # Test the new pytest target
    run_inside_dir("pytest", str(result.project)) == 0


def test_bake_with_no_console_script(cookies):
    context = {"command_line_interface": "No command-line interface"}
    result = cookies.bake(extra_context=context)
    project_path, _, project_dir = project_info(result)

    assert not any(f.name == "cli.py" for f in project_dir.iterdir())
    assert "Click" not in (project_path / "pyproject.toml").read_text()
    
    # Check that script entry points are not present
    pyproject_content = (project_path / "pyproject.toml").read_text()
    assert "tool.poetry.scripts" not in pyproject_content


def test_bake_with_console_script_files(cookies):
    context = {"command_line_interface": "Click"}
    result = cookies.bake(extra_context=context)
    project_path, _, project_dir = project_info(result)

    assert any(f.name == "cli.py" for f in project_dir.iterdir())
    assert "Click" in (project_path / "pyproject.toml").read_text()
    
    # Check for correct script entry point
    pyproject_content = (project_path / "pyproject.toml").read_text()
    assert "python-boilerplate = \"python_boilerplate.cli:main\"" in pyproject_content


def test_bake_with_argparse_console_script_files(cookies):
    context = {"command_line_interface": "Argparse"}
    result = cookies.bake(extra_context=context)
    project_path, _, project_dir = project_info(result)

    assert any(f.name == "cli.py" for f in project_dir.iterdir())
    assert "Click" not in (project_path / "pyproject.toml").read_text()
    
    # Check for correct script entry point
    pyproject_content = (project_path / "pyproject.toml").read_text()
    assert "python-boilerplate = \"python_boilerplate.cli:main\"" in pyproject_content


def test_bake_with_typer_console_script_files(cookies):
    context = {"command_line_interface": "Typer"}
    result = cookies.bake(extra_context=context)
    project_path, _, project_dir = project_info(result)

    assert any(f.name == "cli.py" for f in project_dir.iterdir())
    assert "typer" in (project_path / "pyproject.toml").read_text()
    assert "Click" not in (project_path / "pyproject.toml").read_text()
    
    # Check for correct script entry point
    pyproject_content = (project_path / "pyproject.toml").read_text()
    assert "python-boilerplate = \"python_boilerplate.cli:app\"" in pyproject_content


def test_bake_with_console_script_cli(cookies):
    context = {"command_line_interface": "Click"}
    result = cookies.bake(extra_context=context)
    _, namespace, project_dir = project_info(result)
    module_name = ".".join([namespace, "cli"])
    spec = importlib.util.spec_from_file_location(module_name, project_dir / "cli.py")
    cli = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(cli)
    runner = CliRunner()
    noarg_result = runner.invoke(cli.main)
    assert noarg_result.exit_code == 0
    noarg_output = " ".join(
        [
            "Replace this message by putting your code into",
            result.context["namespace"],
        ]
    )
    assert noarg_output in noarg_result.output
    help_result = runner.invoke(cli.main, ["--help"])
    assert help_result.exit_code == 0
    assert "Show this message" in help_result.output


def test_bake_with_typer_console_script_cli(cookies):
    """Test the Typer CLI."""
    try:
        import typer
        from typer.testing import CliRunner

        context = {"command_line_interface": "Typer"}
        result = cookies.bake(extra_context=context)
        _, namespace, project_dir = project_info(result)
        module_name = ".".join([namespace, "cli"])
        spec = importlib.util.spec_from_file_location(module_name, project_dir / "cli.py")
        cli = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(cli)
        runner = CliRunner()
        result = runner.invoke(cli.app)
        assert result.exit_code == 0
        output = " ".join(
            [
                "Replace this message by putting your code into",
                namespace,
            ]
        )
        assert output in result.stdout
    except ImportError:
        pytest.skip("Typer not available")


def test_pyproject_build_system(cookies):
    result = cookies.bake()

    pyproject = (result.project_path / "pyproject.toml").read_text()

    assert pyproject.startswith(
        dedent(
            """\
        [build-system]
        requires = ["poetry-core"]
        build-backend = "poetry.core.masonry.api"
   """
        )
    )


def test_pyproject_tool_poetry(cookies, faker):
    context = {
        "full_name": faker.name(),
        "email": faker.email(),
        "github_username": faker.user_name(),
        "project_slug": faker.pystr(),
        "namespace": faker.pystr(),
        "project_short_description": faker.sentence(),
        "version": faker.pyint(),
    }
    result = cookies.bake(extra_context=context)

    pyproject = (result.project_path / "pyproject.toml").read_text()

    expected = dedent(
        f"""\
        [tool.poetry]
        name = "{context['project_slug']}"
        description = "{context['project_short_description']}"
        version = "{context['version']}"
        keywords = ["{context['project_slug']}"]
        license = "LICENSE"
        readme = "README.md"
        include = ["LICENSE", "README.md"]
        exclude = ["contrib", "docs", "test*"]
        homepage = "https://github.com/{context['github_username']}/{context['project_slug']}"
        documentation = "https://{context['project_slug']}.readthedocs.io/"
        repository = "https://github.com/{context['github_username']}/{context['project_slug']}"
        authors = [
          "{context['full_name']} <{context['email']}>",
        ]
        packages = [
          {{ include = "{context['namespace']}" }},
        ]
    """
    )
    assert expected in pyproject


def test_pyproject_dependencies(cookies):
    result = cookies.bake()

    pyproject = (result.project_path / "pyproject.toml").read_text()

    expected = dedent(
        """\
        [tool.poetry.dependencies]
        python = ">=3.9"
    """
    )
    assert expected in pyproject


def test_pyproject_dev_dependencies(cookies):
    result = cookies.bake()

    pyproject = (result.project_path / "pyproject.toml").read_text()

    expected = dedent(
        """\
        [tool.poetry.group.dev.dependencies]
        build = "1.2.1"
        bump2version = "1.0.1"
        coverage = "7.4.4"
        faker = "24.8.0"
        pre-commit = "3.7.0"
        pytest = "8.1.1"
        pytest-cov = "5.0.0"
        pytest-mock = "3.14.0"
    """
    )
    assert expected in pyproject


def test_pyproject_docs_dependencies(cookies):
    result = cookies.bake()

    pyproject = (result.project_path / "pyproject.toml").read_text()

    expected = dedent(
        """\
        [tool.poetry.group.docs.dependencies]
        myst-parser = "2.0.0"
        Sphinx = "7.2.6"
        sphinx-rtd-theme = "2.0.0"
    """
    )
    assert expected in pyproject


def test_pyproject_tools(cookies):
    result = cookies.bake()

    pyproject = (result.project_path / "pyproject.toml").read_text()

    expected = dedent(
        """\
        [tool.pytest.ini_options]
        python_files = ["tests.py", "test_*.py", "*_tests.py"]
        addopts = "--doctest-modules"


        [tool.ruff]
        select = ["E", "F", "I"]
        ignore = ["E501"]
        line-length = 88
    """
    )
    assert expected in pyproject
