from agents import Agent
from hooks import CustomRunHooks


class EscalationAgent(Agent):
    """Handles graceful hand‑off to human coaches when escalation is required."""

    def __init__(self, model):
        super().__init__(
            name="EscalationAgent",
            instructions=(
                "You act as a triage assistant.  Whenever a user explicitly asks for a human "
                "or their request is outside policy, escalate the conversation and politely "
                "inform them that a coach will join shortly."
            ),
            model=model,
            tools=[],  # no tools – this agent is purely conversational
            hooks=CustomRunHooks(),
        )
    def run(self, *args, **kwargs):
        """Run the agent with the provided arguments."""
        # Call the parent run method to execute the agent's logic
        return super().run(*args, **kwargs)