import os
import json

DB_FILE = os.path.join(os.path.dirname(__file__), "session_data.json")

def save_session_data(data: dict):
    try:
        with open(DB_FILE, "w") as f:
            json.dump(data, f, indent=4)
    except Exception as e:
        print(f"[DB] Error saving session data: {e}")

def load_session_data():
    if not os.path.exists(DB_FILE):
        return {}
    try:
        with open(DB_FILE, "r") as f:
            return json.load(f)
    except Exception as e:
        print(f"[DB] Error loading session data: {e}")
        return {}
