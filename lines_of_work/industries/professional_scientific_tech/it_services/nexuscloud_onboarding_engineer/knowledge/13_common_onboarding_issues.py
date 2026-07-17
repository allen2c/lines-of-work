title = "Common Onboarding Issues"

content = """
- Issue: Customer subscription not ready (e.g., billing not set). Solution: Send reminder email with link to portal. Escalate if no response in 3 days.
- Issue: IAM permission errors during deployment. Solution: Verify service account has `Owner` role temporarily. Remove after deployment.
- Issue: Quota limits exceeded (e.g., vCPU limit). Solution: Request quota increase via cloud provider console. Typical approval 1-2 hours.
- Issue: Network peering fails due to overlapping CIDR. Solution: Ask customer for non-overlapping CIDR. Use /24 minimum.
- Issue: Backup policy fails because of unsupported VM type. Solution: Check compatibility matrix (NexusCloud Backup Manager). Use alternative method (agent-based backup).
"""

version = "0.0.1"
