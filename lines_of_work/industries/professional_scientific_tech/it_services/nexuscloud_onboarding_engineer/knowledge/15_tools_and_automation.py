title = "Tools and Automation"

content = """
- Primary tools: Terraform (infrastructure as code), Ansible (configuration management), NexusCloud Portal (customer dashboard), GitLab (runbook repository).
- Automation scripts: `deploy_landing_zone.sh` (takes parameters: region, tier, customer name). Must be run from NexusCloud bastion host.
- Monitoring: Prometheus + Grafana for metrics, ELK stack for logs. All dashboards pre-configured per tier.
- Backup: NexusCloud Backup Manager (API-based). Use `backup-cli` for manual restore tests.
- Compliance: NexusCloud Compliance Scanner (CLI). Run `compliance-scan --customer <ID>` before handover.
"""

version = "0.0.1"
