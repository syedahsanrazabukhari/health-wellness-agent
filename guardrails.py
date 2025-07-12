"""Smart validation helpers – filters bad input but allows natural conversation."""
import re
from typing import Any

# List of blocked/inappropriate terms – add more as needed
_BLOCKED_KEYWORDS = [
    "fuck", "shit", "bitch", "asshole", "dumb", "kill", "suicide", "die", "nude", "sex"
]

# Heuristic to check if input seems like a valid sentence or query
def _looks_valid_sentence(text: str) -> bool:
    # Allow short greetings
    if text.lower() in {"hi", "hello", "hey"}:
        return True

    # Accept inputs with a verb (basic check)
    if re.search(r"\b(am|is|are|want|need|have|do|make|build|lose|gain|can|help|like|train|burn|eat|feel|run|walk)\b", text.lower()):
        return True

    return False


def validate_goal_input(user_input: str) -> bool:
    """
    Returns True if the input is:
    - Non-empty
    - Not inappropriate
    - Resembles a normal sentence or query
    """
    if not user_input or len(user_input.strip()) < 2:
        return False

    lowered = user_input.lower()
    if any(bad in lowered for bad in _BLOCKED_KEYWORDS):
        return False

    if not _looks_valid_sentence(user_input):
        return False

    return True


def validate_output(output: Any) -> Any:
    """
    Ensure the agent returns a structured payload (dict or Pydantic).
    If not, wrap in an error dict for logging.
    """
    if isinstance(output, dict) or hasattr(output, "dict"):
        return output
    return {"error": "Invalid output format"}
