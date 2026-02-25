title = "Quản lý Secrets"

content = """
Secrets (API keys, passwords, certs) không được hardcode. Centralized secrets
management. Mekong Delta Tech dùng Vault hoặc cloud-native solution.

**Storage:** Encrypted at rest. Access control. Audit log. Versioning. No plain
text trong code, config file, env var (insecure). Inject at runtime.

**Access Control:** Least privilege. Service chỉ access secret cần thiết.
Role-based. Rotate khi team member rời. Short-lived token khi có thể.

**Rotation:** Rotate secret định kỳ. Automated rotation cho DB password, API key.
Grace period — support cả old và new trong transition. No downtime. Document
rotation procedure.

**Integration:** Service fetch secret từ Vault. Cache với TTL. Handle failure
(fallback, retry). Don't log secret. Secret trong error message = critical bug.
"""  # noqa: E501

version = "0.0.1"
