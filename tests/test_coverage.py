def test_coverage_no(cookies):
    result = cookies.bake(extra_context={"coverage": "No"})

    with open(result.project / ".github" / "workflows" / "python-app.yml") as f:
        content = f.read()
        assert "- run: poetry run pytest" in content
        assert "cov" not in content

    with open(result.project / "README.md") as f:
        content = f.read()
        assert "cov" not in content


def test_coverage_codecov(cookies):
    result = cookies.bake(extra_context={"coverage": "Codecov"})

    with open(result.project / ".github" / "workflows" / "python-app.yml") as f:
        content = f.read()
        assert "poetry run pytest --cov=python_boilerplate" in content
        assert "- uses: codecov/codecov-action@v4.0.1" in content
        assert "token: ${{ secrets.CODECOV_TOKEN }}" in content
        assert "slug: lucasrcezimbra/python-boilerplate" in content

    with open(result.project / "README.md") as f:
        content = f.read()
        assert (
            "[![codecov](https://codecov.io/gh/lucasrcezimbra/python-boilerplate/graph/badge.svg)](https://codecov.io/gh/lucasrcezimbra/python-boilerplate)"
            in content
        )
