title = "Structured Logging"

content = """
Structured log (JSON) cho phép query và aggregate. Essential cho production
debug. Mekong Delta Tech enforce structured logging cho integration services.

**Format:** JSON per line. Fields: timestamp, level, message, correlation_id,
service, extra (key-value). No multiline trong single entry. Parseable.

**What to Log:** Request (method, path, client_id — no sensitive). Response
(status, duration). Error (type, stack). Business event. Context. Don't log
password, token, PII. Redact khi cần. Log sampling cho high volume.

**Correlation:** Mọi log có correlation_id. Trace request qua services. Search
all logs cho request. Include in error response cho client. Propagate.

**Aggregation:** Ship to ELK, Loki, CloudWatch. Index for search. Retention.
Dashboard. Alert on pattern. Cost management cho log volume.
"""  # noqa: E501

version = "0.0.1"
