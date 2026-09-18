from datetime import datetime

logs = []

event_types = [
    "Login Success",
    "Login Failure",
    "File Access",
    "Privilege Escalation",
    "Intrusion Alert",
    "Config Change",
]

statuses = ["Success", "Failure", "Blocked", "Unknown"]

risk_levels = ["Low", "Medium", "High"]

log_keys = [
    "log_id",
    "timestamp",
    "username",
    "event_type",
    "status",
    "source",
    "target",
    "risk_level",
    "description",
]

SAVE_FILE = "data/cladts_logs.json"


def now_timestamp():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def next_log_id():
    highest = 0
    for record in logs:
        if not isinstance(record, dict):
            continue
        value = record.get("log_id", 0)
        if isinstance(value, bool):
            continue
        if isinstance(value, int) and value > highest:
            highest = value
    return highest + 1


def find_log_by_id(log_id):
    for record in logs:
        if isinstance(record, dict) and record.get("log_id") == log_id:
            return record
    return None


def make_log(username, event_type, status, source, target, risk_level, description):
    record = {
        "log_id": next_log_id(),
        "timestamp": now_timestamp(),
        "username": username,
        "event_type": event_type,
        "status": status,
        "source": source,
        "target": target,
        "risk_level": risk_level,
        "description": description,
    }
    logs.append(record)
    return record


def format_log(log):
    if not isinstance(log, dict):
        return "Invalid log record."
    labels = {
        "log_id": "Log ID",
        "timestamp": "Timestamp",
        "username": "Username",
        "event_type": "Event Type",
        "status": "Status",
        "source": "Source",
        "target": "Target",
        "risk_level": "Risk Level",
        "description": "Description",
    }
    lines = []
    for key in log_keys:
        lines.append(f"{labels[key]:<12}: {log.get(key, '')}")
    return "\n".join(lines)


def is_valid_log(record):
    if not isinstance(record, dict):
        return False
    for key in log_keys:
        if key not in record:
            return False
    log_id = record.get("log_id")
    if isinstance(log_id, bool) or not isinstance(log_id, int):
        return False
    for key in log_keys:
        if key == "log_id":
            continue
        if not isinstance(record.get(key), str):
            return False
    if record.get("event_type") not in event_types:
        return False
    if record.get("status") not in statuses:
        return False
    if record.get("risk_level") not in risk_levels:
        return False
    return True

def load_logs(path):
    

    import json

    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
    except (OSError, ValueError) as error:
        print("Could not load file: " + str(error))
        return 0

    if not isinstance(data, list):
        print("File does not contain a list of logs.")
        return 0

    loaded = 0
    for item in data:
        if is_valid_log(item):
            logs.append(item)
            loaded += 1

    return loaded


def save_logs(path):
    
    import json

    try:
        with open(path, "w", encoding="utf-8") as f:
            json.dump(logs, f, indent=2)
        return True
    except (OSError, TypeError, ValueError) as error:
        print("Could not save file: " + str(error))
        return False

LOGS = logs
EVENT_TYPES = event_types
STATUSES = statuses
RISK_LEVELS = risk_levels