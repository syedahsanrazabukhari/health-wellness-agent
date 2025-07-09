from agents import function_tool

@function_tool
def recommend_workout_based_on_goal(fitness_target: str = "general fitness") -> str:
    return f"For {fitness_target}, do 30 mins walk + 20 mins strength training."