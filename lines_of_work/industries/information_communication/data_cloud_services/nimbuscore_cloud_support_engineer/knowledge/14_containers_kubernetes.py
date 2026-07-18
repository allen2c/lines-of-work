title = "Managed Kubernetes (NCS-K8s) Troubleshooting"

content = """
- Pod stuck in `Pending`: check node capacity, PVC binding, and taints/tolerations. Use `kubectl describe pod` and look at the `Events` section last.
- `ImagePullBackOff`: the most common cause is a missing or revoked image pull secret; the second most common is an ECR-equivalent endpoint not being reachable from a private subnet.
- Node not `Ready` for more than 5 minutes: drain the workload with `kubectl drain <node> --ignore-daemonsets --delete-emptydir-data` and replace it.
- Control plane API server throttling starts at 400 requests per second per account; bursts above this get HTTP 429.
- Upgrade cycles: Kubernetes minor versions are supported for 14 months after GA on NimbusCore. Customers on unsupported versions receive a 90-day deprecation notice.
"""  # noqa: E501

version = "0.0.1"
