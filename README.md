# LangChain Agent

**ReAct agent scaffold powered by Ollama (setup only).**

This project provides a minimal scaffold for building a ReAct (Reasoning + Acting) agent using LangChain and Ollama. The current version includes only the project setup and structure—no business logic has been implemented yet.

## Features

- 🤖 ReAct agent architecture with LangChain
- 🦙 Ollama integration for local LLM inference
- 🛠️ Extensible tool system
- ✨ Pre-configured with modern Python tooling (ruff, black, mypy, pytest)
- 🔄 CI/CD pipeline with GitHub Actions
- 🪝 Pre-commit hooks for code quality

## Prerequisites

- Python 3.11+
- [Ollama](https://ollama.ai/) installed and running locally
- Git
- GitHub CLI (`gh`) for repository creation (optional)

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/YOUR_USERNAME/langchain-agent.git
   cd langchain-agent
   ```

2. **Set up virtual environment and install dependencies:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install --upgrade pip
   pip install -e ".[dev]"
   ```

3. **Configure environment variables:**
   ```bash
   cp .env.example .env
   # Edit .env with your Ollama settings if needed
   ```

## Environment Variables

Create a `.env` file in the project root:

```env
OLLAMA_BASE_URL=http://localhost:11434
OLLAMA_MODEL=llama3.1:8b
```

## Development

### Pre-commit Hooks

Install pre-commit hooks to ensure code quality:

```bash
make precommit-install
# or
pre-commit install
```

### Code Formatting

Format code with black and ruff:

```bash
make format
```

### Linting

Run ruff linter:

```bash
make lint
```

### Type Checking

Run mypy type checker:

```bash
make typecheck
```

### Testing

Run pytest test suite:

```bash
make test
```

### Run All Checks

```bash
make lint && make typecheck && make test
```

## Project Structure

```
langchain-agent/
├── README.md
├── LICENSE
├── .gitignore
├── .env.example
├── pyproject.toml
├── .pre-commit-config.yaml
├── ruff.toml
├── mypy.ini
├── Makefile
├── .github/
│   └── workflows/
│       └── ci.yml
├── src/
│   └── langchain_agent/
│       ├── __init__.py
│       ├── config.py
│       ├── agent/
│       │   ├── __init__.py
│       │   ├── planner.py
│       │   └── tools/
│       │       ├── __init__.py
│       │       └── example_tool.py
│       └── cli.py
└── tests/
    └── test_smoke.py
```

## Usage

Run the CLI (currently a placeholder):

```bash
make run
# or
langchain-agent --version
```

## Makefile Commands

- `make setup` - Set up virtual environment and install dependencies
- `make format` - Format code with black and ruff
- `make lint` - Run ruff linter
- `make typecheck` - Run mypy type checker
- `make test` - Run pytest
- `make precommit-install` - Install pre-commit hooks
- `make run` - Run the CLI
- `make clean` - Clean up cache and temp files

## CI/CD

The project includes a GitHub Actions workflow that runs on every push and pull request:

- Code linting with ruff
- Code formatting check with black
- Type checking with mypy
- Unit tests with pytest

## TODO

This is a scaffold project. The following functionality needs to be implemented:

- [ ] ReAct agent implementation in `planner.py`
- [ ] Ollama LLM integration
- [ ] Custom tools for the agent
- [ ] Agent execution loop
- [ ] CLI commands for agent interaction
- [ ] Additional tests

## License

MIT License - see [LICENSE](LICENSE) file for details.

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Run tests and linting
5. Submit a pull request

## Resources

- [LangChain Documentation](https://python.langchain.com/)
- [Ollama Documentation](https://ollama.ai/)
- [ReAct Paper](https://arxiv.org/abs/2210.03629)
