title = "Resource Tagging Standards"

content = """
- Mandatory tags: `Customer` (e.g., `acme-corp`), `Environment` (`dev`, `staging`, `prod`), `CostCenter` (from customer), `Project` (e.g., `migration-2025`), `Owner` (email of customer contact).
- Optional tags: `Compliance` (e.g., `SOC2`), `BackupPolicy` (e.g., `daily-7day`), `MaintenanceWindow` (e.g., `Sun-0200`).
- Tags must be applied at resource creation. Use Terraform `tags` block. Engineer must enforce via policy (e.g., AWS Config rule).
- Missing tags cause compliance failure. Engineer must fix before handover. Use NexusCloud Tag Auditor tool.
- Tag values must be lowercase, no spaces. Use hyphens for multi-word.
"""

version = "0.0.1"
