def format_stream_output(step: dict) -> str:
    if "error" in step:
        return f"Error Occurred: {step['error']}"
    return str(step)