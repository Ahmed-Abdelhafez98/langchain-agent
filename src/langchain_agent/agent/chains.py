"""Chain builders for the ReAct agent."""

from langchain_core.agents import AgentAction
from langchain_core.runnables import Runnable
from langchain_core.tools import BaseTool
from langchain_ollama import OllamaLLM

from .parsers import ReActOutputParser
from .prompts import create_react_prompt


def format_log_to_str(intermediate_steps: list[tuple[AgentAction, str]]) -> str:
    """Format intermediate steps (agent actions and observations) to string.

    This is the equivalent of langchain.agents.format_scratchpad.log.format_log_to_str
    which is not available in newer versions.

    Args:
        intermediate_steps: List of tuples (AgentAction, observation)

    Returns:
        Formatted string for agent scratchpad
    """
    if not intermediate_steps:
        return ""

    thoughts = ""
    for action, observation in intermediate_steps:
        thoughts += action.log
        thoughts += f"\nObservation: {observation}\nThought: "
    return thoughts


def create_agent_chain(
    tools: list[BaseTool], model: str = "gpt-oss:20b", temperature: float = 0
) -> Runnable:
    """Create an agent chain that processes input and returns AgentAction or AgentFinish.

    Args:
        tools: List of tools available to the agent
        model: Ollama model name
        temperature: LLM temperature setting

    Returns:
        A runnable chain that takes input and agent_scratchpad and returns parsed output
    """
    # Create prompt
    prompt = create_react_prompt(tools)

    # Create LLM
    # Note: stop parameter removed - it can cause empty responses with some models
    llm = OllamaLLM(model=model, temperature=temperature)

    # Build chain
    agent: Runnable = (
        {
            "input": lambda x: x["input"],
            "agent_scratchpad": lambda x: format_log_to_str(x.get("agent_scratchpad", [])),
        }
        | prompt
        | llm
        | ReActOutputParser()
    )

    return agent
