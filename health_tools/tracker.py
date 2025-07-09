from agents import function_tool

@function_tool
def monitor_progress(parameter: str = "steps") -> str:
    return f"Tracking {parameter}: Stay consistent!"

def initiate_tracking_tool():
    return "Tool for tracking health metrics."