title = "Runbook Structure"

content = """
- Each runbook must contain: Customer name, environment details, architecture diagram, resource inventory, configuration parameters, and operational procedures.
- Sections: Overview, Prerequisites, Deployment Steps, Monitoring, Backup, Security, Troubleshooting, Escalation Contacts.
- Use NexusCloud Runbook Generator tool. Input: customer ID, tier, region. Output: Markdown file with placeholders.
- Engineer must fill placeholders with actual values (IPs, resource names, URLs). Review with customer before handover.
- Runbook versioning: use Git repository. Each handover creates a tagged release (e.g., v1.0). Updates after handover managed by operations.
"""

version = "0.0.1"
