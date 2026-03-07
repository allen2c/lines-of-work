"""Release quality gates to enforce standards before deployment."""

title = "Release Quality Gates"

content = """
Quality gates are automated or manual checks that must pass before a release proceeds.
Gates prevent known-bad changes from reaching production.

**Automated Gates:** Unit tests, integration tests, static analysis, security scans, dependency
checks, build success. Configure in CI/CD; block merge or deploy on failure. Gates should
run in reasonable time to avoid blocking velocity.

**Manual Gates:** Code review approval, security review (for sensitive changes), product
sign-off, operations readiness. Document who approves and what they check. Use checklists
to reduce subjectivity.

**Gate Configuration:** Define gates per service or release type. Critical services may have
stricter gates. Document gate bypass process for emergencies; require post-facto review.
"""

version = "0.0.1"
