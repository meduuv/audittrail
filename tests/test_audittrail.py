from audittrail import filter_events, normalize, summarize

def test_audit():
    event = normalize({"actor": " admin ", "action": "login", "outcome": "SUCCESS"})
    assert event["actor"] == "admin"
    events = [event, {"actor": "guest", "action": "login", "outcome": "failure"}]
    assert len(filter_events(events, action="login")) == 2
    assert summarize(events)["total"] == 2
