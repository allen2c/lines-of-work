title = "Backup and Disaster Recovery"

content = """
- Standard backup: daily snapshot of all VMs and databases, retention 7 days. Stored in same region. Restore RTO 4 hours, RPO 24 hours.
- Premium: hourly backups for critical VMs, retention 30 days. Cross-region replication. RTO 2 hours, RPO 1 hour.
- Enterprise: continuous backup (every 15 minutes) for databases, retention 90 days. Multi-region failover. RTO 30 minutes, RPO 15 minutes.
- Backup policies defined in NexusCloud Backup Manager. Engineer must test restore monthly for Premium/Enterprise.
- Disaster recovery plan: document failover steps, contact list, and runbook. Test annually with customer.
"""

version = "0.0.1"
