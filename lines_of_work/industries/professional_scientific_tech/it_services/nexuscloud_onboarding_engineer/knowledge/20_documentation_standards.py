title = "Documentation Standards"

content = """
- All documentation must follow NexusCloud Style Guide: use active voice, numbered steps for procedures, screenshots for complex UIs.
- Runbook: use Markdown. Include table of contents, version history, and glossary. Maximum 50 pages.
- Architecture diagrams: use Draw.io or Lucidchart. Export as PNG and embed in runbook. Must show all network segments, security groups, and data flows.
- Naming conventions: resources named as `{customer}-{env}-{resource-type}-{number}` (e.g., `acme-prod-vm-01`). Tags mandatory.
- Documentation reviewed by peer engineer before handover. Use NexusCloud Doc Review tool.
"""

version = "0.0.1"
