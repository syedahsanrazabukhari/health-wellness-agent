from agents import function_tool, RunContextWrapper
from pydantic import BaseModel
from typing import List
import datetime

class CheckInSchedule(BaseModel):
    reminders: List[str]

@function_tool
async def schedule_checkins(ctx: RunContextWrapper) -> CheckInSchedule:
    goal_period = (ctx.context.goal or {}).get("period", "1 month")
    try:
        number, unit = goal_period.split()
        number = int(number)
    except Exception:
        number, unit = 1, "month"

    schedule = []
    start_date = datetime.date.today()

    for i in range(number):
        next_date = start_date + datetime.timedelta(days=i * (30 if unit.startswith("month") else 7))
        schedule.append(f"Check-in reminder on {next_date.strftime('%Y-%m-%d')}")

    return CheckInSchedule(reminders=schedule)
