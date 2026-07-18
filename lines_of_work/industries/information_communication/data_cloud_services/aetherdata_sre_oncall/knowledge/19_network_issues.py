title = "Network Issue Troubleshooting"

content = """
- Common symptoms: high latency, packet loss, connection timeouts.
- First step: check the network dashboard for bandwidth utilization and error counters.
- Use `mtr` to trace route to affected services. Look for packet loss at intermediate hops.
- If internal network issue, check switch and router logs. Escalate to network team if needed.
- If external (cloud provider), check provider status page and open a support ticket.
- For DNS issues, verify DNS resolution using `dig` and check DNS server health.
"""  # noqa: E501

version = "0.0.1"
