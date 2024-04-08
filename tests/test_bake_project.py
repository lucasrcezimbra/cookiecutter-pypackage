import importlib
import os
import shlex
import subprocess
from contextlib import contextmanager

import pytest
from click.testing import CliRunner


@contextmanager
def inside_dir(dirpath):
    """
    Execute code from inside the given directory
    :param dirpath: String, path of the directory the command is being run.
    """
    old_path = os.getcwd()
    try:
        os.chdir(dirpath)
        yield
    finally:
        os.chdir(old_path)


def run_inside_dir(command, dirpath):
    """
    Run a command from inside a given directory, returning the exit status
    :param command: Command that will be executed
    :param dirpath: String, path of the directory the command is being run.
    """
    with inside_dir(dirpath):
        return subprocess.check_call(shlex.split(command))


def project_info(result):
    """Get toplevel dir, project_slug, and project dir from baked cookies"""
    project_slug = os.path.split(result.project_path)[-1]
    project_dir = result.project_path / project_slug
    return result.project_path, project_slug, project_dir


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


def test_bake_with_console_script_files(cookies):
    context = {"command_line_interface": "Click"}
    result = cookies.bake(extra_context=context)
    project_path, _, project_dir = project_info(result)

    assert any(f.name == "cli.py" for f in project_dir.iterdir())
    assert "Click" in (project_path / "pyproject.toml").read_text()


def test_bake_with_argparse_console_script_files(cookies):
    context = {"command_line_interface": "Argparse"}
    result = cookies.bake(extra_context=context)
    project_path, _, project_dir = project_info(result)

    assert any(f.name == "cli.py" for f in project_dir.iterdir())
    assert "Click" not in (project_path / "pyproject.toml").read_text()


def test_bake_with_console_script_cli(cookies):
    context = {"command_line_interface": "Click"}
    result = cookies.bake(extra_context=context)
    _, project_slug, project_dir = project_info(result)
    module_name = ".".join([project_slug, "cli"])
    spec = importlib.util.spec_from_file_location(module_name, project_dir / "cli.py")
    cli = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(cli)
    runner = CliRunner()
    noarg_result = runner.invoke(cli.main)
    assert noarg_result.exit_code == 0
    noarg_output = " ".join(
        ["Replace this message by putting your code into", project_slug]
    )
    assert noarg_output in noarg_result.output
    help_result = runner.invoke(cli.main, ["--help"])
    assert help_result.exit_code == 0
    assert "Show this message" in help_result.output
