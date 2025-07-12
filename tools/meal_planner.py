from agents import function_tool


@function_tool
def meal_planner(diet: str = "balanced") -> str:
    """Produce a high‑level meal plan summary for the requested diet style."""
    return (
        f"🥗 *{diet.capitalize()}* meal plan → base every plate around 🍗 protein, 🥦 veggies, "
        "whole‑grain carbs, and 💧 plenty of water."
    )


def generate_meal_plan():
     return "(future) macro‑calculated meal plan"
