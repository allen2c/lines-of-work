title = "Quotas, Limits, and Increase Requests"

content = """
- Soft limits exist on most regional and per-account resources (e.g., VPCs per region = 5 default, running vCPUs per region = 5 default on t-series).
- Quota increase requests are submitted via the Console and routed to the Capacity team; standard SLA is 1 business day, expedited is 4 hours with manager approval.
- Customers hitting the on-demand vCPU limit must understand that quota increases do not guarantee capacity in a specific AZ.
- For predictable bursts (events, migrations, ML training), recommend Reserved Capacity or Savings Plans instead of repeated quota increases.
- Never promise a quota increase approval time; only state the SLA target.
"""  # noqa: E501

version = "0.0.1"
