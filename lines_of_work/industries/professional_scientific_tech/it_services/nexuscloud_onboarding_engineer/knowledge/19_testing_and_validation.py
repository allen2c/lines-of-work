title = "Testing and Validation"

content = """
- After landing zone deployment, run automated tests: network connectivity (ping between subnets), IAM permissions (create/delete test resource), backup (trigger manual backup).
- Use NexusCloud Test Suite: `test-suite run --customer <ID>`. Tests take ~30 minutes. Report generated with pass/fail.
- For Premium/Enterprise, also test disaster recovery: simulate region failure (using script) and verify failover. Must be done in non-production environment.
- Validation checklist: all resources tagged, monitoring alerts active, backup policy applied, security baseline compliant. Engineer signs off.
- Customer may request additional tests (e.g., load test). Coordinate with performance team.
"""

version = "0.0.1"
