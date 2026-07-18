title = "Transaction Monitoring Thresholds"

content = """
- Velocity check: >5 transactions from same account within 10 minutes triggers alert. >10 within 1 hour triggers critical.
- Amount thresholds: single transaction >$2,000 for new accounts (<30 days old) flagged; >$10,000 for any account requires manual review.
- Cross-border transactions: any international transfer >$1,000 flagged for AML review.
- Card testing: >3 small declines ($0.50-$5) within 5 minutes triggers immediate block.
"""  # noqa: E501

version = "0.0.1"
