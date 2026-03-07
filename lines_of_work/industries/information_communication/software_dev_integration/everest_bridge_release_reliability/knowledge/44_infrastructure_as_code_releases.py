"""Infrastructure as code and release coordination."""

title = "Infrastructure as Code Releases"

content = """
Infrastructure changes (Terraform, CloudFormation, etc.) should follow release discipline.
Treat IaC as part of the release: version it, test it, and deploy it in a controlled sequence.

**Ordering:** Typically deploy infrastructure changes before or with application changes that
depend on them. Use feature flags or backward-compatible changes to avoid big-bang cutovers.

**Testing:** Validate IaC in non-production first. Use plan/diff review before apply. For
destructive changes, require explicit approval and staged rollout.

**Rollback:** Infrastructure rollback can be complex. Prefer additive changes; document
revert procedures. Keep state backups and use version control for all IaC.
"""

version = "0.0.1"
