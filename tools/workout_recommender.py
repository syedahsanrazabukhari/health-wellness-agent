from agents import function_tool, RunContextWrapper
from pydantic import BaseModel
from typing import List

class WorkoutSuggestions(BaseModel):
    exercises: List[str]

@function_tool
async def recommend_workout(ctx: RunContextWrapper, injury_detail: str = "") -> WorkoutSuggestions:
    injury = injury_detail.lower()
    suggestions = []

    if "knee" in injury:
        suggestions = [
            "Gentle cycling",
            "Swimming or water aerobics",
            "Straight leg raises",
            "Wall sits",
            "Step-ups"
        ]
    elif "back" in injury:
        suggestions = [
            "Pelvic tilts",
            "Cat-cow stretches",
            "Bridges",
            "Partial crunches",
            "Bird-dog exercises"
        ]
    elif "shoulder" in injury:
        suggestions = [
            "Pendulum stretches",
            "Crossover arm stretches",
            "Shoulder blade squeezes",
            "Wall push-ups",
            "External rotation with resistance band"
        ]
    else:
        suggestions = [
            "Walking",
            "Bodyweight squats",
            "Light jogging",
            "Yoga stretches",
            "Core strengthening exercises"
        ]

    return WorkoutSuggestions(exercises=suggestions)
