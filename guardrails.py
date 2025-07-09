import re
from typing import Any

def is_valid_goal_input(text: str) -> bool:
    # Matches inputs like "lose 5kg in 2 months" or "gain muscle"
    regex = r"^(lose|gain)\s+\d+\w*\s*(in\s*\d+\s*(month|week)s?)?.*$"
    return bool(re.match(regex, text.lower())) or "muscle" in text.lower()

def ensure_valid_output(output: Any) -> Any:
    # Accept dicts or objects with .dict() method, else return error dict
    if isinstance(output, dict) or hasattr(output, "dict"):
        return output
    return {"error": "Output format invalid"}
import re
from typing import Any

def is_valid_goal_input(text: str) -> bool:
    regex = r"^(lose|gain)\s+\d+\w*\s*(in\s*\d+\s*(month|week)s?)?.*$"
    return bool(re.match(regex, text.lower())) or "muscle" in text.lower()

def ensure_valid_output(output: Any) -> Any:
    if isinstance(output, dict) or hasattr(output, "dict"):
        return output
    return {"error": "Output format invalid"}