"""Output parsers for ReAct agent."""

import re

from langchain_core.agents import AgentAction, AgentFinish
from langchain_core.output_parsers import BaseOutputParser


class ReActOutputParser(BaseOutputParser):
    """Parse ReAct-style LLM output into AgentAction or AgentFinish."""

    def parse(self, text: str) -> AgentAction | AgentFinish:
        """Parse LLM output into structured agent action or finish.

        Args:
            text: The raw text output from the LLM

        Returns:
            AgentAction if the agent wants to use a tool, or AgentFinish if complete

        Raises:
            ValueError: If the output cannot be parsed
        """
        # Check for Final Answer
        if "Final Answer:" in text:
            return AgentFinish(
                return_values={"output": text.split("Final Answer:")[-1].strip()},
                log=text,
            )

        # Parse Action and Action Input
        action_match = re.search(r"Action:\s*(.+?)(?:\n|$)", text, re.IGNORECASE)
        action_input_match = re.search(
            r"Action Input:\s*(.+?)(?:\n|$)", text, re.IGNORECASE | re.DOTALL
        )

        if not action_match:
            raise ValueError(f"Could not parse action from: {text}")

        action = action_match.group(1).strip()
        action_input = action_input_match.group(1).strip() if action_input_match else ""

        return AgentAction(tool=action, tool_input=action_input, log=text)
