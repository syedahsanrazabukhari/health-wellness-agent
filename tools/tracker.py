from agents import function_tool, RunContextWrapper
from pydantic import BaseModel
from datetime import datetime

class ProgressEntry(BaseModel):
    timestamp: str
    note: str

@function_tool
async def track_progress(ctx: RunContextWrapper, log: str) -> ProgressEntry:
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    entry = {"timestamp": now, "note": log}
    ctx.context.progress_logs.append(entry)
    return ProgressEntry(timestamp=now, note=log)
