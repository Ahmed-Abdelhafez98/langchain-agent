"""Command-line interface for LangChain Agent."""

import argparse
import sys

from langchain_agent import __version__


def main():
    """Main CLI entry point."""
    parser = argparse.ArgumentParser(
        prog="langchain-agent",
        description="ReAct agent scaffold powered by Ollama",
    )
    parser.add_argument(
        "--version",
        action="version",
        version=f"%(prog)s {__version__}",
    )

    parser.parse_args()

    # TODO: Implement CLI commands for agent interaction
    print("LangChain Agent CLI - Setup complete (no business logic yet)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
