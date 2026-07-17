title = "Landing Zone Templates"

content = """
- Three pre-built templates: Basic (single VPC/VNet, 3 subnets), Standard (hub-spoke with transit gateway, 5 subnets), Advanced (multi-region with VPN/ExpressRoute, 10+ subnets).
- Each template includes: network ACLs, security groups, flow logs, CloudTrail/Activity Logs, encryption at rest (CMK), and default IAM roles.
- Deployment via NexusCloud Terraform modules (version 4.2+). Parameters: region, CIDR blocks, customer name, environment (dev/staging/prod).
- Customization allowed only for Premium/Enterprise. Must be approved by architecture team via change request.
- Template selection based on customer tier and number of workloads. Use Basic for <20 resources, Standard for 20-100, Advanced for >100.
"""

version = "0.0.1"
