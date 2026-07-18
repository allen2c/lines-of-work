title = "IAM Identity, Roles, and Authentication Troubleshooting"

content = """
- NimbusCore IAM has three principal types: Root User, IAM User, and Service Identity (used by compute, functions, and managed services).
- Authentication failures fall into four buckets: wrong credentials, expired/rotated keys, missing MFA, and policy denial.
- When a customer reports "Access Denied", always run the IAM Policy Simulator first against the exact action, resource, and condition keys; do not guess from the policy text alone.
- For Service Identity issues, ask the customer to attach the `NC-Troubleshooter` role temporarily to the workload's instance profile or function execution role.
- Never ask the customer to paste their secret access key; ask them to confirm the last 4 characters of the key ID instead.
"""  # noqa: E501

version = "0.0.1"
