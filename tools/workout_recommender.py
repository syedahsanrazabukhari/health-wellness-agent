from agents import function_tool


@function_tool
def workout_recommender(goal: str = "general fitness") -> str:
    """Return a quick workout outline tailored to the specified goal."""
    return (
        f"💪 For **{goal}**, try 30 min brisk walking plus 4×5 body‑weight strength moves each day."
    )
