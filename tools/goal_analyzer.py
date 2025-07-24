from agents import function_tool, RunContextWrapper
from pydantic import BaseModel
import re

class GoalAnalysis(BaseModel):
    amount: float
    unit: str
    period: str
    summary: str

@function_tool
async def analyze_health_goal(wrapper: RunContextWrapper, description: str) -> GoalAnalysis:
    text = description.lower()

    weight_loss_terms = ["lose weight", "fat loss", "reduce weight", "slim"]
    weight_gain_terms = ["gain weight", "increase weight", "bulk", "build muscle"]
    fitness_terms = ["fitness", "exercise", "stamina", "cardio"]
    general_terms = ["health", "wellness", "lifestyle"]

    if any(term in text for term in weight_loss_terms):
        goal_type = "Weight Loss"
    elif any(term in text for term in weight_gain_terms):
        goal_type = "Weight Gain"
    elif any(term in text for term in fitness_terms):
        goal_type = "Fitness"
    elif any(term in text for term in general_terms):
        goal_type = "General Health"
    else:
        goal_type = "Unspecified"

    amount_match = re.search(r"(\d+\.?\d*)\s*(kg|lbs|pounds|kilograms)?", text)
    amount = float(amount_match.group(1)) if amount_match else 0.0
    unit = amount_match.group(2) if amount_match and amount_match.group(2) else ""

    duration_match = re.search(r"(\d+)\s*(day|week|month|year)s?", text)
    period = f"{duration_match.group(1)} {duration_match.group(2)}{'s' if int(duration_match.group(1)) > 1 else ''}" if duration_match else ""

    wrapper.context.goal = {
        "type": goal_type,
        "amount": amount,
        "unit": unit,
        "period": period,
        "description": description.strip()
    }

    return GoalAnalysis(amount=amount, unit=unit, period=period, summary=goal_type)
