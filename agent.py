from agents import Agent
from health_tools.goal_analyzer import analyze_user_goal
from health_tools.meal_planner import create_meal_plan
from health_tools.workout_recommender import recommend_workout_based_on_goal
from health_tools.scheduler import schedule_health_check
from health_tools.tracker import monitor_progress

from custom_agents.nutrition_expert_agent import DietGuidanceAdvisor
from custom_agents.injury_support_agent import RehabFitnessAdvisor
from custom_agents.escalation_agent import HumanSupportEscalator

from hooks import CustomRunHooks

def build_health_wellness_agent(model_instance):
    return Agent(
        name="WellnessPlannerAgent",
        instructions=(
            "Help users with goals, plans, tracking, and escalate to experts when needed."
        ),
        model=model_instance,
        tools=[
            analyze_user_goal,
            create_meal_plan,
            recommend_workout_based_on_goal,
            monitor_progress,
            schedule_health_check,
        ],
        handoffs=[
            DietGuidanceAdvisor(model_instance),
            RehabFitnessAdvisor(model_instance),
            HumanSupportEscalator(model_instance)
        ],
        hooks=CustomRunHooks(),
    )
