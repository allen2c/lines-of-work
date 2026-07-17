title = "Change Management Process"

content = """
- Any deviation from standard landing zone template requires a change request (CR). CR must include: description, impact assessment, rollback plan.
- CR approval: Standard changes (e.g., adding a subnet) approved by lead engineer. Major changes (e.g., new region) approved by architecture team.
- Change window: Standard changes can be applied during business hours. Major changes require a maintenance window (weekend or after hours).
- Engineer must document all changes in runbook and update Git repository. Use NexusCloud Change Manager tool.
- Emergency changes (e.g., security patch) can bypass normal process but must be documented within 24 hours.
"""

version = "0.0.1"
