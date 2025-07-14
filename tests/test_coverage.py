def test_coverage_no(cookies):
    result = cookies.bake(extra_context={"coverage": "No"})

    with open(result.project / ".github" / "workflows" / "python-app.yml") as f:
        content = f.read()
        assert "- run: make test" in content
        assert "cov" not in content

    with open(result.project / "README.md") as f:
        content = f.read()
        assert "cov" not in content

    with open(result.project / "Makefile") as f:
        content = f.read()
        assert ".PHONY: build lint run test\n" in content
        assert "cov" not in content


def test_coverage_codecov(cookies):
    result = cookies.bake(extra_context={"coverage": "Codecov"})

    with open(result.project / ".github" / "workflows" / "python-app.yml") as f:
        content = f.read()
        assert "make test-cov" in content
        assert "- uses: codecov/codecov-action@v4.0.1" in content
        assert "token: ${{ secrets.CODECOV_TOKEN }}" in content
        assert "slug: lucasrcezimbra/python-boilerplate" in content

    with open(result.project / "README.md") as f:
        content = f.read()
        assert (
            "[![codecov](https://codecov.io/gh/lucasrcezimbra/python-boilerplate/graph/badge.svg)](https://codecov.io/gh/lucasrcezimbra/python-boilerplate)"
            in content
        )

    with open(result.project / "Makefile") as f:
        content = f.read()
        assert ".PHONY: build lint run test test-cov\n" in content
        assert "test-cov:" in content
        assert "poetry run pytest --cov=python_boilerplate" in content


def test_copilot_setup_steps_workflow(cookies):
    """Test that the copilot-setup-steps.yml workflow file is created and has correct content."""
    result = cookies.bake()

    workflow_path = result.project / ".github" / "workflows" / "copilot-setup-steps.yml"
    assert workflow_path.exists(), "copilot-setup-steps.yml workflow file should exist"

    with open(workflow_path) as f:
        content = f.read()

        # Check basic structure
        assert 'name: "Copilot Setup Steps"' in content
        assert "copilot-setup-steps:" in content  # job name
        assert "runs-on: ubuntu-latest" in content
        assert "permissions:" in content
        assert "contents: read" in content

        # Check triggers
        assert "workflow_dispatch:" in content
        assert "push:" in content
        assert "pull_request:" in content
        assert ".github/workflows/copilot-setup-steps.yml" in content

        # Check steps
        assert "uses: actions/checkout@v4" in content
        assert "pipx install poetry" in content
        assert "uses: actions/setup-python@v5" in content
        assert 'python-version: "3.9"' in content
        assert 'cache: "poetry"' in content
        assert "make install" in content

        # Check that there are no comments (as requested in the issue)
        assert "#" not in content, "Workflow file should not contain any comments"
