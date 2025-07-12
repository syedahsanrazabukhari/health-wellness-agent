from agents import Agent
from tools.workout_recommender import workout_recommender
from hooks import CustomRunHooks


class InjurySupportAgent(Agent):
    """Suggests modified exercise plans that respect injury constraints."""

    def __init__(self, model):
        super().__init__(
            name="InjurySupportAgent",
            instructions=(
                "You are an Injury‑Aware Fitness Coach.  Provide gentle, evidence‑based "
                "workout routines tailored to common injuries and recovery stages."
            ),
            model=model,
            tools=[workout_recommender],
            hooks=CustomRunHooks(),
        )
    def run(self, *args, **kwargs):
        """Run the agent with the provided arguments."""
        # Call the parent run method to execute the agent's logic
        return super().run(*args, **kwargs)