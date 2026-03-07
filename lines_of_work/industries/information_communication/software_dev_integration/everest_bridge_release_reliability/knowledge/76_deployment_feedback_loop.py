"""Deployment feedback loop for continuous improvement."""

title = "Deployment Feedback Loop"

content = """
A feedback loop captures deployment outcomes and feeds them back into release processes.
This improves future releases and reduces repeat failures.

**Data Collection:** Track deployment success/failure, rollback frequency, time to
deploy, and post-deploy incident rate. Correlate with release characteristics (size,
complexity, team).

**Analysis:** Review deployment metrics in release retrospectives. Identify patterns:
which changes cause rollbacks, which gates catch issues, which stages fail most often.

**Action:** Update runbooks, add gates, improve tests, or adjust processes based on
findings. Share learnings across teams. Celebrate improvements in deployment
reliability.
"""

version = "0.0.1"
