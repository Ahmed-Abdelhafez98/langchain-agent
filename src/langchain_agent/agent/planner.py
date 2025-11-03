"""ReAct agent planner module.

This module contains helper functions for the ReAct agent.
"""


from langchain_core.tools import BaseTool


def find_tool_by_name(name: str, tools: list[BaseTool]) -> BaseTool:
    """Find a tool by its name.

    Args:
        name: The name of the tool to find
        tools: List of available tools

    Returns:
        The tool with the matching name

    Raises:
        ValueError: If no tool with the given name is found
    """
    for tool in tools:
        if tool.name == name:
            return tool
    raise ValueError(f"Tool with name {name} not found")
