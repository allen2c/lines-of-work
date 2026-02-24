title = "Blue-Green Deployment"

content = """
Blue-green: two identical environment. Switch traffic at once. Instant rollback.
Alternative to canary. Mekong Delta Tech use khi canary không phù hợp.

**Setup:** Blue (current), Green (new). Deploy to green. Smoke test. Switch
LB to green. Blue becomes standby. Next deploy: deploy to blue, switch to blue.
Alternate.

**Switch:** DNS, load balancer, router. Atomic. No gradual. All or nothing.
Session drain. Connection drain. Ensure clean switch. No request to old
during switch.

**Rollback:** Switch back to previous. Fast. No redeploy. Data compatibility
critical — both version support same data. DB migration: both support old
and new schema during transition.

**Integration:** API deployment. Zero downtime. Partner không thấy interruption.
Test green thoroughly before switch. Document process.
"""  # noqa: E501

version = "0.0.1"
