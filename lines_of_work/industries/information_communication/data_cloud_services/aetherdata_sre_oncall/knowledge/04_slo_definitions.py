title = "Service Level Objectives (SLOs)"

content = """
- **API Availability**: 99.99% uptime measured over a 30-day rolling window. Excludes planned maintenance.
- **API Latency**: p99 < 200ms for read requests, p99 < 500ms for write requests.
- **Data Durability**: 99.999999999% (11 nines) for object storage, measured annually.
- **Database Throughput**: 99.9% of queries complete within 1 second for standard tier.
- SLOs are defined per service in the SLO dashboard (Grafana). Each service has a separate SLO panel.
- SLO compliance is reviewed monthly in the SRE team meeting.
"""  # noqa: E501

version = "0.0.1"
