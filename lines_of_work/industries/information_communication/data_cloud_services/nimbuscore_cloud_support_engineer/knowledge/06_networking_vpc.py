title = "VPC, Subnets, Route Tables, and Security Groups"

content = """
- A customer cannot reach a new instance in 90% of "I just launched it and cannot connect" tickets because the attached security group has no inbound rule, or the NACL is implicitly denying.
- Order of checks: Security Group → NACL → Route Table → Internet Gateway / NAT Gateway → local subnet route.
- Each NimbusCore VPC supports up to 500 route table entries per route table; the soft warning threshold is 80% (400 entries).
- The default VPC is for quick starts only; production workloads must use a custom VPC with at least two AZs and non-overlapping CIDR.
- When a customer reports asymmetric connectivity, capture a `Reachability Analyzer` path between the two ENIs before changing any rule.
"""  # noqa: E501

version = "0.0.1"
