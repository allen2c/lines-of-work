title = "Môi trường Sandbox"

content = """
Sandbox cho phép client test integration mà không ảnh hưởng production. Mekong
Delta Tech cung cấp sandbox với data và behavior tương tự production.

**Data:** Synthetic data, anonymized, hoặc seed data. Không real PII. Reset
định kỳ hoặc on-demand. Document data available. Có thể có scenario-specific
seed (success, error cases).

**Behavior:** Sandbox mimic production logic. Same validation. Có thể mock
external dependency. Rate limit có thể relaxed. Fake payment, notification.
Document differences từ production.

**Access:** Separate credentials. Apply for sandbox access. Same auth mechanism
(OAuth, API key). Different base URL. Clear documentation. Support channel
cho sandbox issue.

**Testing:** Client test full flow. Verify before production onboarding.
Automated test chạy against sandbox. Sandbox stability = production stability.
"""  # noqa: E501

version = "0.0.1"
