from agents import Agent
from output_guardrails import health_output_guardrail
from input_guardrails import health_input_guardrail

from tools.goal_analyzer import analyze_health_goal
from tools.meal_planner import plan_meals
from tools.workout_recommender import recommend_workout
from tools.tracker import track_progress
from tools.scheduler import schedule_checkins

from custom_agents.nutrition_expert_agent import nutrition_expert_agent
from custom_agents.injury_support_agent import injury_support_agent
from custom_agents.escalation_agent import escalation_agent

from hooks import CustomRunHooks

def create_health_agent(model):
    nutrition_agent = nutrition_expert_agent
    injury_agent = injury_support_agent
    escalation_agent_ref = escalation_agent

    return Agent(
        name="HealthWellnessAgent",
        instructions=(
            "You are a helpful Health & Wellness Assistant. Assist users by understanding and breaking down "
            "complex queries into actionable tasks like goal analysis, meal planning, workout recommendations, "
            "progress tracking, and scheduling check-ins. Use specialized agents when necessary. "
            "Keep tone supportive and clear."
        ),
        model=model,
        tools=[
            analyze_health_goal,
            plan_meals,
            recommend_workout,
            track_progress,
            schedule_checkins
        ],
        handoffs=[nutrition_agent, injury_agent, escalation_agent_ref],
        hooks=CustomRunHooks(),
        input_guardrails=[health_input_guardrail],
        output_guardrails=[health_output_guardrail]
    )
