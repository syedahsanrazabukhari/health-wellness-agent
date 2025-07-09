from agents import Agent
from health_tools.meal_planner import create_meal_plan
from hooks import CustomRunHooks

class DietGuidanceAdvisor(Agent):
    def __init__(self, llm_model):
        super().__init__(
            name="DietGuidanceAdvisor",
            instructions="Support users with dietary restrictions by generating suitable meal plans.",
            model=llm_model,
            tools=[create_meal_plan],
            hooks=CustomRunHooks()
        )