from typing import List, Optional, Dict
from pydantic import BaseModel

class SessionContext(BaseModel):
    user_name: str
    user_id: int
    target_goal: Optional[dict] = None
    diet_choices: Optional[str] = None
    exercise_plan: Optional[dict] = None
    meal_suggestions: Optional[List[str]] = None
    injury_details: Optional[str] = None
    handoff_history: List[str] = []
    progress_updates: List[Dict[str, str]] = []