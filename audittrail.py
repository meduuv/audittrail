"""Offline audit event processing helpers."""

def normalize(event):
    return {"actor": str(event.get("actor", "unknown")).strip(), "action": str(event.get("action", "unknown")).strip(), "outcome": str(event.get("outcome", "unknown")).strip().lower()}

def filter_events(events, actor=None, action=None, outcome=None):
    return [e for e in events if (actor is None or e.get("actor") == actor) and (action is None or e.get("action") == action) and (outcome is None or e.get("outcome") == outcome)]

def summarize(events):
    outcomes = {}
    for event in events:
        key = str(event.get("outcome", "unknown")).lower()
        outcomes[key] = outcomes.get(key, 0) + 1
    return {"total": len(events), "outcomes": outcomes}
