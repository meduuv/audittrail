# AuditTrail

> Normalize and summarize audit events for defensive logging workflows.

AuditTrail is a small Python utility for turning loosely structured audit-event data into consistent records that can be filtered and summarized.

## Features

- Normalize audit-event records
- Filter by actor
- Filter by action
- Filter by outcome
- Summarize event activity
- Keep processing local and deterministic

## Workflow

```text
audit events
     ↓
normalize
     ↓
filter
     ↓
aggregate
     ↓
report
```

## Example

```python
from audittrail import normalize, summarize

records = [normalize(event) for event in events]
print(summarize(records))
```

Use the source and tests as the authoritative API reference.

## Scope

AuditTrail is designed for analysis and reporting of event data you are authorized to handle. It does not connect to systems or alter logs.

## Development

```bash
python -m pytest
```

## License

MIT. See `LICENSE`.

## Author

Built by **Medu** · https://guns.lol/meduu