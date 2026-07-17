title = "Disaster Recovery Planning"

content = """
- For each customer, engineer must create a DR plan document: RTO/RPO, failover steps, contact list, and testing schedule.
- Standard tier: DR plan is basic - restore from backup in same region. No automated failover.
- Premium: automated failover to secondary region using NexusCloud DR Orchestrator. Test quarterly.
- Enterprise: active-active multi-region with traffic manager. Continuous replication. Test monthly.
- DR plan must be included in runbook. Engineer must conduct a tabletop exercise with customer during handover for Premium/Enterprise.
- If customer has on-premises DR, coordinate with NexusCloud Hybrid team.
"""

version = "0.0.1"
