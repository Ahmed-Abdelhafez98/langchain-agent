"""Tool implementations for the ReAct agent."""

from langchain_core.tools import tool


@tool
def get_text_length(text: str) -> int:
    """Returns the length of the text in characters.

    Args:
        text: The input text to measure

    Returns:
        The number of characters in the text
    """
    text = text.strip()  # Remove leading/trailing whitespace and newlines
    # Remove matching quote pairs
    if len(text) >= 2 and text[0] == text[-1] and text[0] in ('"', "'"):
        text = text[1:-1]
    return len(text)


@tool
def example_tool(query: str) -> str:
    """Example tool that returns a simple response.

    Args:
        query: The input query string

    Returns:
        A formatted response string
    """
    return f"Example tool received: {query}"
