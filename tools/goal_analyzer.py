from agents import function_tool


@function_tool
def goal_analyzer(goal: str) -> str:
    """Return an encouraging reformulation of the user‑supplied goal."""
    return f"🎯 Awesome target: **{goal}** – let's map out a game‑plan!"