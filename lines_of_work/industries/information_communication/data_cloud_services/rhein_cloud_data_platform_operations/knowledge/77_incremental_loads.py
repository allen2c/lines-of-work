title = "Incremental Load Strategies"

content = """
Incremental loads process only new or changed data since the last run. Common
strategies: watermark columns, change data capture, and date-range filters.
Correct watermark selection is critical; errors cause duplicates or gaps.
Operations verify watermark consistency and handle late-arriving data
according to SLA.
"""

version = "0.0.1"
