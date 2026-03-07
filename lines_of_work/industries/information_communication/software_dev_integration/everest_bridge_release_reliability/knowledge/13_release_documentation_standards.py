"""Release documentation standards knowledge item."""

title = "Release Documentation Standards"

content = """
Release documentation provides an auditable record of what was deployed, when, and why. It
supports incident response, compliance, and continuous improvement.

**Release Notes:** Each release has notes listing changes by category: new features, fixes,
deprecations, and breaking changes. Notes are written for operators and stakeholders, not only
developers. Include migration guidance for breaking changes.

**Deployment Record:** Log the deployment timestamp, artifact versions, environment, and
responsible party. Link to the pipeline run, commit hashes, and change tickets.

**Rollback Instructions:** Document the rollback procedure for each release. Include the
previous stable version, rollback commands, and verification steps. Update if the procedure
changes.

**Runbook Updates:** If a release introduces new operational procedures, update runbooks before
deployment. Link runbook sections to the release notes.

**Retention:** Retain release documentation for the period required by compliance and
incident review. Archive in a searchable system. Ensure accessibility for on-call and
audit teams.
"""

version = "0.0.1"
