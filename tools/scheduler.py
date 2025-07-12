from agents import function_tool


@function_tool
def checkin_scheduler(day: str = "Sunday") -> str:
    """Return a friendly confirmation for a scheduled check‑in."""
    return f"📅 Your next health check‑in is booked for **{day}** at 10 AM.  See you then!"


def schedule_checkins():
    """Placeholder – could integrate with calendar APIs later."""
    return "(future) repeated calendar event"