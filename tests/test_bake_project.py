import importlib
import os
import shlex
import subprocess
from contextlib import contextmanager
from pathlib import Path

import pytest
from click.testing import CliRunner
from cookiecutter.utils import rmtree


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


@contextmanager
def bake_in_temp_dir(cookies, *args, **kwargs):
    """
    Delete the temporal directory that is created when executing the tests
    :param cookies: pytest_cookies.Cookies,
        cookie to be baked and its temporal files will be removed
    """
    result = cookies.bake(*args, **kwargs)
    try:
        yield result
    finally:
        rmtree(str(result.project))


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
    project_path = Path(result.project)
    project_slug = os.path.split(project_path)[-1]
    project_dir = project_path / project_slug
    return project_path, project_slug, project_dir


def test_bake_with_defaults(cookies):
    with bake_in_temp_dir(cookies) as result:
        assert result.project.isdir()
        assert result.exit_code == 0
        assert result.exception is None

        found_toplevel_files = [f.basename for f in result.project.listdir()]
        assert "pyproject.toml" in found_toplevel_files
        assert "python_boilerplate" in found_toplevel_files
        assert "tests" in found_toplevel_files


@pytest.mark.skip("TODO: fix")
def test_bake_and_run_tests(cookies):
    with bake_in_temp_dir(cookies) as result:
        assert result.project.isdir()
        run_inside_dir("python setup.py test", str(result.project)) == 0
        print("test_bake_and_run_tests path", str(result.project))


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
        with bake_in_temp_dir(
            cookies, extra_context={"open_source_license": license}
        ) as result:
            assert target_string in result.project.join("LICENSE").read()
            assert classifier in result.project.join("pyproject.toml").read()


def test_bake_not_open_source(cookies):
    with bake_in_temp_dir(
        cookies, extra_context={"open_source_license": "Not open source"}
    ) as result:
        found_toplevel_files = [f.basename for f in result.project.listdir()]
        assert "LICENSE" not in found_toplevel_files
        assert "License" not in result.project.join("README.md").read()
        assert "License" not in result.project.join("pyproject.toml").read()


@pytest.mark.skip("TODO: fixme")
def test_using_pytest(cookies):
    with bake_in_temp_dir(
        cookies,
    ) as result:
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

    with open(project_path / "pyproject.toml") as setup_file:
        assert "Click" not in setup_file.read()


def test_bake_with_console_script_files(cookies):
    context = {"command_line_interface": "Click"}
    result = cookies.bake(extra_context=context)
    project_path, _, project_dir = project_info(result)

    assert any(f.name == "cli.py" for f in project_dir.iterdir())

    with open(project_path / "pyproject.toml") as f:
        assert "Click" in f.read()


def test_bake_with_argparse_console_script_files(cookies):
    context = {"command_line_interface": "Argparse"}
    result = cookies.bake(extra_context=context)
    project_path, _, project_dir = project_info(result)

    assert any(f.name == "cli.py" for f in project_dir.iterdir())

    with open(project_path / "pyproject.toml") as f:
        assert "Click" not in f.read()


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
