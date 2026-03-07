"""Version control for releases knowledge item."""

title = "Version Control for Releases"

content = """
Version control is the source of truth for what goes into a release. Consistent tagging,
branching, and commit hygiene enable reproducible builds and clear release lineage.

**Release Tags:** Tag each release with a semantic version (e.g. v1.2.3) or release
identifier. Tags must point to the exact commit that was built and deployed. Never
move or overwrite release tags.

**Branch Strategy:** Use a main or master branch as the release baseline. Feature branches
merge via pull requests. Release branches may be used for stabilization; merge back to
main to avoid divergence.

**Commit Messages:** Use conventional commits or a consistent format. Link commits to
tickets. This supports changelog generation and traceability from production back to
source.
"""

version = "0.0.1"
