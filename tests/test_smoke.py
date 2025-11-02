"""Smoke tests for basic package functionality."""

from langchain_agent import __version__
from langchain_agent.config import Config


def test_version():
    """Test that version is defined."""
    assert __version__ == "0.1.0"


def test_config_defaults():
    """Test that config loads with default values."""
    config = Config()
    assert config.ollama_base_url == "http://localhost:11434"
    assert config.ollama_model == "llama3.1:8b"


def test_config_import():
    """Test that config can be imported from main module."""
    from langchain_agent.config import config

    assert config is not None
    assert hasattr(config, "ollama_base_url")
    assert hasattr(config, "ollama_model")
