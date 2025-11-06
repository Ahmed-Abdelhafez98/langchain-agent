"""Simple example demonstrating the ReAct agent."""

from dotenv import load_dotenv
from langchain_agent.agent import create_agent_chain, find_tool_by_name
from langchain_agent.agent.tools import get_text_length
from langchain_core.agents import AgentAction, AgentFinish

load_dotenv()


def main():
    """Run a simple ReAct agent example."""
    # Setup tools
    tools = [get_text_length]

    # Initialize intermediate steps tracking
    intermediate_steps = []

    print("\n--- Agent Setup ---")
    print(f"Available tools: {[t.name for t in tools]}")

    # Create agent chain
    agent = create_agent_chain(tools, model="gpt-oss:20b", temperature=0)

    # Invoke agent with a question
    input_dict = {
        "input": "What is the length of the text 'Egypt'?",
        "agent_scratchpad": intermediate_steps,
    }
    agent_step: AgentAction | AgentFinish = agent.invoke(input_dict)
    print(agent_step)

    # Execute tool if agent returned an action
    if isinstance(agent_step, AgentAction):
        tool_name = agent_step.tool
        tool_to_use = find_tool_by_name(tool_name, tools)
        tool_input = agent_step.tool_input

        observation = tool_to_use.invoke(str(tool_input))
        print(f"\nObservation: {observation}")
        intermediate_steps.append((agent_step, str(observation)))

    agent_step: AgentAction | AgentFinish = agent.invoke(
        {"input": "What is the length of the text 'Egypt'?", "agent_scratchpad": intermediate_steps}
    )
    print(agent_step)


if __name__ == "__main__":
    main()
