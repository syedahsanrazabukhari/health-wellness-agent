from agents import Agent
from health_tools.workout_recommender import recommend_workout_based_on_goal
from hooks import CustomRunHooks

class RehabFitnessAdvisor(Agent):
    def __init__(self, llm_model):
        super().__init__(
            name="RehabFitnessAdvisor",
            instructions="Provide injury-safe workout routines and fitness suggestions.",
            model=llm_model,
            tools=[recommend_workout_based_on_goal],
            hooks=CustomRunHooks()
        )