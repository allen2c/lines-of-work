title = "Quản lý Dependency"

content = """
Integration phụ thuộc nhiều service. Dependency management — version, update,
vulnerability. Mekong Delta Tech có process cho dependency hygiene.

**Version Pinning:** Pin exact version trong lock file. Reproducible build.
Update deliberate. Changelog review. Test after update. Automated PR cho
minor/patch update (Dependabot).

**Vulnerability Scanning:** Scan dependencies cho CVE. Fix critical/high
timely. Update hoặc patch. Ignore khi false positive (document). SBOM
(Software Bill of Materials) cho compliance.

**Transitive Dependencies:** Direct và transitive. Transitive có thể pull
vulnerable. Use tools (npm audit, pip-audit). Minimal dependency. Prefer
well-maintained library.

**Integration Client:** HTTP client, Kafka client — keep updated. API client
version match server. Compatibility matrix. Test version combination.
"""  # noqa: E501

version = "0.0.1"
