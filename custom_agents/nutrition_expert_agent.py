from agents import Agent
from tools.meal_planner import meal_planner
from hooks import CustomRunHooks


class NutritionExpertAgent(Agent):
    """Recommends meal plans accounting for allergies, diabetes, etc."""

    def __init__(self, model):
        super().__init__(
            name="NutritionExpertAgent",
            instructions=(
                "You are a Registered Dietitian.  Craft balanced meal plans and substitutions "
                "for users who have medical or cultural dietary restrictions."
            ),
            model=model,
            tools=[meal_planner],
            hooks=CustomRunHooks(),
        )
    def run(self, *args, **kwargs):
        """Run the agent with the provided arguments."""
        # Call the parent run method to execute the agent's logic
        return super().run(*args, **kwargs)