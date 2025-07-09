from agents import function_tool

@function_tool
def schedule_health_check(day_name: str = "Sunday") -> str:
    return f"Check-in scheduled on {day_name} at 10 AM."

def setup_checkin_reminders():
    return "Utility for scheduling health reminders."   