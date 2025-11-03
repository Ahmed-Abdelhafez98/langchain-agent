"""Chain builders for the ReAct agent."""


from langchain_core.runnables import Runnable
from langchain_core.tools import BaseTool
from langchain_ollama import OllamaLLM

from .parsers import ReActOutputParser
from .prompts import create_react_prompt


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
    llm = OllamaLLM(model=model, temperature=temperature, stop=["\nObservation:"])

    # Build chain
    agent = (
        {"input": lambda x: x["input"], "agent_scratchpad": lambda x: x.get("agent_scratchpad", "")}
        | prompt
        | llm
        | ReActOutputParser()
    )

    return agent
