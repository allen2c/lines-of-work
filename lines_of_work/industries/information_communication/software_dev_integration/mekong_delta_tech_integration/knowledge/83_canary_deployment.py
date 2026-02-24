title = "Canary Deployment"

content = """
Canary: deploy new version cho subset traffic. Validate trước full rollout.
Integration update cần careful rollout. Mekong Delta Tech dùng canary cho
API change.

**Mechanism:** Route X% traffic to new version. Based on header, user id,
random. Compare metrics. Auto rollback on anomaly. Gradual increase. 100%.

**Metrics:** Error rate, latency, throughput. Compare canary vs baseline.
Statistical significance. Duration. Alert on regression. Business metric.

**Integration:** API version canary. New integration endpoint. Partner
migration. Reduce risk. Quick rollback. Document canary process. Partner
opt-in khi cần.

**Challenges:** Stateful? Session affinity. Database migration? Backward
compatible. Config. Feature flag complement. Rollback procedure tested.
"""  # noqa: E501

version = "0.0.1"
