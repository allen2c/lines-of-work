"""Deployment window management knowledge item."""

title = "Deployment Window Management"

content = """
Deployment windows are scheduled periods when releases may be executed. Define windows based on
business patterns: avoid peak usage, align with maintenance expectations, and respect timezone
constraints for global systems. Communicate windows to stakeholders and enforce them in pipeline
config. Allow emergency overrides with approval. Track actual deployment duration to refine
future window sizing. Document blackout periods (e.g. fiscal close, major events).
"""

version = "0.0.1"
