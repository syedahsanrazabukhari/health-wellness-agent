from agents import function_tool


@function_tool
def progress_tracker(metric: str = "steps") -> str:
    """Send back a motivational nudge for the metric being tracked."""
    return f"📊 Tracking **{metric}** – keep the momentum rolling!"


def track_progress():
    """Placeholder – hook into persistent storage later."""
    return "(future) persisted progress log"
