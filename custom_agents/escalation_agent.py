from agents import Agent
from hooks import CustomRunHooks

class HumanSupportEscalator(Agent):
    def __init__(self, llm_model):
        super().__init__(
            name="HumanSupportEscalator",
            instructions="Assist users in escalating their concerns to a human coach when needed.",
            model=llm_model,
            tools=[],
            hooks=CustomRunHooks()
        )