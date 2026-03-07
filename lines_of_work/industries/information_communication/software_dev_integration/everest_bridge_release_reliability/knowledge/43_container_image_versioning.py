"""Container image versioning for releases."""

title = "Container Image Versioning"

content = """
Container images must be versioned and immutable for reproducible deployments. Use semantic
versioning or commit-based tags (e.g. v1.2.3 or sha-abc1234). Avoid latest for production.

**Tagging Strategy:** Prefer unique tags per build. Include metadata: build number, git
commit, build date. Enables quick identification of what is running and supports rollback.

**Registry:** Store images in a private registry with access controls. Scan images for
vulnerabilities before promotion. Use digest (sha256) for exact pinning when needed.

**Lifecycle:** Define retention for old images. Keep at least the last N production versions
for rollback. Document which images are approved for production deployment.
"""

version = "0.0.1"
