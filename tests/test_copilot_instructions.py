"""Tests for copilot-instructions.md file."""

import os
from pathlib import Path


def test_copilot_instructions_exists():
    """Test that copilot-instructions.md exists in the repository root."""
    repo_root = Path(__file__).parent.parent
    copilot_instructions_path = repo_root / "copilot-instructions.md"
    
    assert copilot_instructions_path.exists(), "copilot-instructions.md should exist in repository root"


def test_copilot_instructions_content():
    """Test that copilot-instructions.md contains expected content."""
    repo_root = Path(__file__).parent.parent
    copilot_instructions_path = repo_root / "copilot-instructions.md"
    
    content = copilot_instructions_path.read_text()
    
    # Check for key sections
    assert "# GitHub Copilot Instructions" in content
    assert "Cookiecutter template repository" in content
    assert "Template Structure" in content
    assert "Generated Project Features" in content
    assert "Template Variables" in content
    assert "cookiecutter.json" in content
    
    # Check for important technical details
    assert "Poetry" in content
    assert "Black" in content
    assert "Ruff" in content
    assert "pytest" in content
    assert "Sphinx" in content
    
    # Check for cookiecutter-specific guidance
    assert "{{" in content  # Jinja2 templating syntax
    assert "cookiecutter.project_slug" in content
    
    # Ensure it's not empty
    assert len(content.strip()) > 1000, "copilot-instructions.md should contain substantial content"