title = "EC2-equivalent Instance Lifecycle and Common Failures"

content = """
- Instance states: `pending`, `running`, `stopping`, `stopped`, `shutting-down`, `terminated`. A stuck `pending` beyond 10 minutes usually indicates capacity or EBS volume attach issues.
- Instance launch failures: `InsufficientInstanceCapacity` (retry in another AZ), `VcpuLimitExceeded` (request quota increase), `KeyPair not found` (region mismatch).
- Status checks: `SystemStatusCheckFailed` is a NimbusCore-side issue and warrants a `Stop & Start` to migrate the instance; `InstanceStatusCheckFailed` is a customer-side OS issue.
- For a rebooted-but-stuck instance, capture the system log via `nc-get-console-output --latest` and the screenshot via `nc-get-console-screenshot` before recommending any action.
- Customer-initiated stop/start preserves the instance ID; terminate does not. Make this distinction explicit when the customer is debating which action to take.
"""  # noqa: E501

version = "0.0.1"
