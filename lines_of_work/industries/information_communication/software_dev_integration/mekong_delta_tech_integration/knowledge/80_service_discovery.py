title = "Service Discovery"

content = """
Service discovery tìm địa chỉ service động. Microservices, container. Integration
cần discover upstream. Mekong Delta Tech dùng service discovery trong K8s.

**Patterns:** Client-side (client query registry). Server-side (LB route).
DNS-based. K8s: DNS name, service. Consul, etcd. Choose per infrastructure.

**Health:** Discovery integrate với health. Unhealthy instance không trong
rotation. Refresh. Deregister on shutdown. Avoid sending to dead instance.

**Integration:** Client config với service name. Resolve at runtime. No
hardcode IP. Failover. Multiple instance. Load balance. Cache với TTL.
Re-resolve on failure.

**Multi-environment:** Different registry per env. Sandbox, prod. Config.
Test discovery. Fallback khi registry down. Document discovery setup.
"""  # noqa: E501

version = "0.0.1"
