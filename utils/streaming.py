
def stream_response(step: dict) -> str:
    """Render any streaming step, handling errors cleanly."""
    if step.get("error"):
        return f"🚨 Error: {step['error']}"
    return str(step)