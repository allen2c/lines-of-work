title = "Velocity Checks and Limits"

content = """
- Per-account velocity: max 10 transactions per hour, 50 per day. Exceeding triggers temporary hold.
- Per-IP velocity: max 20 transactions per hour from same IP. If exceeded, block IP for 1 hour.
- Per-device velocity: max 5 accounts created from same device in 24 hours. Triggers manual review.
- Velocity rules are adjusted dynamically based on historical fraud patterns (e.g., holiday season looser limits).
"""  # noqa: E501

version = "0.0.1"
