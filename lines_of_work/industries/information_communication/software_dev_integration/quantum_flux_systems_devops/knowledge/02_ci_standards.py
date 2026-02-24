title = "Continuous Integration (CI) Standards"

content = """
At Quantum Flux Systems, Continuous Integration (CI) is the mechanism that ensures code quality and stability before any change reaches our shared branches. Every commit triggers a series of automated checks designed to catch regressions and enforce our engineering standards.

**Automated Testing:** CI pipelines must include unit tests, integration tests, and static analysis. We aim for high code coverage, but prioritize the quality and relevance of tests over raw percentages. Tests must be deterministic; flaky tests are treated as high-priority bugs and must be fixed or quarantined immediately.

**Fast Feedback Loops:** CI pipelines are optimized for speed. Developers should receive feedback on their changes within minutes. We achieve this through parallel test execution, efficient caching of dependencies, and selective testing based on modified files.

**Static Analysis and Linting:** We use automated linters and static analysis tools to enforce consistent coding styles and identify potential security vulnerabilities or performance bottlenecks early in the development cycle.

**Build Artifacts:** Successful CI runs produce immutable build artifacts (e.g., Docker images, binaries). These artifacts are versioned and stored in a central registry, ensuring that the exact same code tested in CI is what eventually runs in production.

**Merge Requirements:** No code is merged into the main branch without a successful CI pass and a peer review. This "green build" policy is strictly enforced to maintain the integrity of our codebase.
"""  # noqa: E501

version = "0.0.1"
