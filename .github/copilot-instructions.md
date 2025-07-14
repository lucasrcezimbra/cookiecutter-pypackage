# GitHub Copilot Instructions

## Project Overview

This is a **Cookiecutter template repository** for creating opinionated Python packages. It is not a regular Python project but a template that generates Python package projects with a comprehensive, production-ready setup.

## Template Structure

- `cookiecutter.json`: Configuration file defining template variables
- `{{cookiecutter.project_slug}}/`: Template directory containing the generated project structure
- `hooks/`: Post-generation hooks for project setup
- `tests/`: Tests for the cookiecutter template itself (not the generated projects)

## Generated Project Features

When this template is used, it creates Python packages with:

### Development Tools
- **Package Management**: Poetry (`pyproject.toml`)
- **Code Formatting**: Black
- **Code Linting**: Ruff (replaces flake8, isort, etc.)
- **Pre-commit Hooks**: Automated code quality checks
- **Version Management**: bump2version

### Testing & Quality
- **Testing Framework**: pytest with pytest-mock
- **Coverage**: Codecov integration (optional)
- **Faker**: For generating test data

### Documentation
- **Documentation Generator**: Sphinx
- **ReadTheDocs**: Integration ready (`.readthedocs.yaml`)

### CI/CD
- **GitHub Actions**:
  - `python-app.yml`: Test automation
  - `python-publish.yml`: PyPI publishing
- **Dependabot**: Automated dependency updates

### Project Structure Generated
```
project_name/
├── CHANGELOG.md
├── docs/
│   ├── conf.py
│   ├── index.rst
│   └── Makefile
├── .github/workflows/
├── .gitignore
├── LICENSE
├── pyproject.toml
├── README.md
├── package_name/
│   ├── __init__.py
│   └── package_name.py
└── tests/
    └── test_package_name.py
```

## Template Variables

Key cookiecutter variables (from `cookiecutter.json`):
- `full_name`: Author's full name
- `email`: Author's email
- `github_username`: GitHub username
- `project_name`: Human-readable project name
- `project_slug`: URL/directory-friendly project name
- `namespace`: Python package name (underscores)
- `command_line_interface`: CLI framework choice (None, Click, Argparse)
- `open_source_license`: License selection
- `coverage`: Coverage service choice (Codecov, None)

## Coding Guidelines for This Template

### When modifying template files:
1. Use Jinja2 templating syntax: `{{ cookiecutter.variable_name }}`
2. Conditional blocks: `{% if cookiecutter.option == "value" %}`
3. File naming with variables: `{{cookiecutter.namespace}}/`

### When modifying tests:
- Use `pytest-cookies` for testing cookiecutter templates
- Test different variable combinations in `cookiecutter.json`
- Verify generated project structure and content

### Code Style for Template:
- Follow the same style as generated projects (Black, Ruff)
- Use Poetry for dependency management
- Include comprehensive docstrings
- Write tests for template functionality

## Common Tasks

### Adding new template variables:
1. Add to `cookiecutter.json`
2. Use in template files with `{{ cookiecutter.new_variable }}`
3. Add tests in `tests/test_bake_project.py`

### Modifying generated project structure:
1. Edit files in `{{cookiecutter.project_slug}}/`
2. Update documentation examples
3. Add corresponding tests

### Updating dependencies:
1. Modify `{{cookiecutter.project_slug}}/pyproject.toml`
2. Update this project's `pyproject.toml` if needed
3. Test with `poetry run pytest`

## Best Practices

1. **Minimal Changes**: Keep the template focused and opinionated
2. **Testing**: Always test template changes with different variable combinations
3. **Documentation**: Update README.md when adding features

## Development Workflow

1. Make changes to template files
2. Run tests: `poetry run pytest`
3. Test template generation: `cookiecutter .`
4. Verify generated project works correctly
5. Update documentation if needed

## Notes for AI Assistance

- This is a **template repository**, not a regular Python project
- Focus on Jinja2 templating and cookiecutter best practices
- Consider the generated project's needs, not this repository's runtime needs
- Test both the template functionality and generated project quality
- Respect the opinionated nature - maintain consistency with established patterns
