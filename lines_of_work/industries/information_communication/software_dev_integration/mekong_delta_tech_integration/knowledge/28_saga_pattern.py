title = "Saga Pattern"

content = """
Saga pattern quản lý distributed transaction qua nhiều service. Mỗi service thực
hiện local transaction. Compensation khi có failure. Không có 2PC (two-phase commit).

**Choreography:** Mỗi service listen event, thực hiện, emit event tiếp. No central
orchestrator. Simple nhưng hard to understand flow. Service coupling qua events.

**Orchestration:** Central orchestrator gọi từng service, quyết định next step.
Easier to understand. Single point of failure. Orchestrator state machine.

**Compensation:** Mỗi step có compensation (reverse action). Order khi step 3 fail,
compensate step 2, 1. Compensation có thể fail — cần retry, manual intervention.
Design compensation cẩn thận. Idempotent compensation.

**Challenges:** No atomicity. Eventual consistency. Handle duplicate events.
Visibility vào saga state. Consider saga visualization và monitoring.
"""  # noqa: E501

version = "0.0.1"
