.PHONY: setup format lint typecheck test precommit-install run clean help

VENV_BIN := venv/Scripts
PYTHON := $(VENV_BIN)/python
PIP := $(VENV_BIN)/pip

help:
	@echo "LangChain Agent - Available targets:"
	@echo "  setup             - Set up virtual environment and install dependencies"
	@echo "  format            - Format code with black and ruff"
	@echo "  lint              - Run ruff linter"
	@echo "  typecheck         - Run mypy type checker"
	@echo "  test              - Run pytest"
	@echo "  precommit-install - Install pre-commit hooks"
	@echo "  run               - Run the CLI (placeholder)"
	@echo "  clean             - Clean up cache and temp files"

setup:
	python -m venv venv
	$(PIP) install --upgrade pip
	$(PIP) install -e ".[dev]"
	@echo "Setup complete! Activate venv with: venv\\Scripts\\activate"

format:
	$(PYTHON) -m black src tests
	$(PYTHON) -m ruff check --fix src tests

lint:
	$(PYTHON) -m ruff check src tests

typecheck:
	$(PYTHON) -m mypy src

test:
	$(PYTHON) -m pytest tests -v

precommit-install:
	$(PYTHON) -m pre_commit install

run:
	$(PYTHON) -m langchain_agent.cli

clean:
	rm -rf build dist *.egg-info
	rm -rf .ruff_cache .mypy_cache .pytest_cache
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
