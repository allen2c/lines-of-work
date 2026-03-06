title = "Rollback Procedures"

content = """
Rollback steps are documented in each pipeline runbook. Typical sequence:
stop new jobs, revert code/config, restore from backup if data corrupted,
validate, communicate. Time-to-rollback targets vary by criticality.
"""

version = "0.0.1"
