from agents import function_tool

@function_tool
def create_meal_plan(plan_type: str = "balanced") -> str:
    return f" Your {plan_type} meal includes proteins, fiber, and hydration."

def suggest_meal_structure():
    return "Helps design meal plans based on dietary needs."