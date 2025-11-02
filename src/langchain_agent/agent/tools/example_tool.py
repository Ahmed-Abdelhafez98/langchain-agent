"""Example tool implementation.

This is a stub tool that demonstrates the structure for
creating custom tools for the ReAct agent.
"""

from langchain.tools import tool


@tool
def example_tool(query: str) -> str:
    """Example tool that returns a simple response.

    Args:
        query: The input query string

    Returns:
        A formatted response string
    """
    return f"Example tool received: {query}"
