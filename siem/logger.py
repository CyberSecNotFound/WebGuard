import json, datetime

def log_event(data):
    print(json.dumps({
        "timestamp": datetime.datetime.utcnow().isoformat(),
        "event": "webguard_scan",
        "data": data
    }))
