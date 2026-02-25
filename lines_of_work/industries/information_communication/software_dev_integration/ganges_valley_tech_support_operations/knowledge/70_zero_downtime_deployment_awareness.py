title = "Zero-Downtime Deployment Awareness"

content = """
Modern products deploy frequently with
minimal or no downtime. Support should
understand deployment patterns to set
expectations and troubleshoot.

**Deployment Windows:** Some products
deploy during low-traffic hours. Brief
blips or redirects may occur. Document
and communicate when known.

**Feature Flags:** New features may
roll out gradually. Users in different
cohorts may see different behavior.
Avoid implying inconsistency is a bug
until rollout is confirmed complete.

**Rollback:** If a deployment causes
issues, Engineering may roll back.
Support communicates status without
speculating on cause.
"""  # noqa: E501

version = "0.0.1"
