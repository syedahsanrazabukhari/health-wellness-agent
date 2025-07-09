from agents import function_tool

@function_tool
def analyze_user_goal(user_goal: str) -> str:
    return f"Goal noted: '{user_goal}' looks motivating and achievable!"