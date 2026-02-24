title = "Catalog Integration Pattern"

content = """
Pattern catalog tổng hợp pattern dùng cho integration. Reference. Mekong
Delta Tech maintain pattern catalog. Developer consult khi design.

**Request-Response:** Sync. REST, gRPC. Simple. Coupling. Timeout. Retry.
Circuit breaker. Use khi cần immediate result.

**Fire-and-Forget:** Async. Message queue. Decouple. No immediate response.
Eventual. Use cho notification, non-critical. Idempotent consumer.

**Request-Reply (Async):** Request, return correlation ID. Poll or callback.
Long operation. Use khi sync timeout. Document poll/callback.

**Event-Driven:** Publish event. Consumers subscribe. Loose coupling. Ordering?
Consistency? Saga. Use cho audit, notification, sync. Schema evolution.

**Choreography vs Orchestration:** Who coordinate? Choreography: events.
Orchestration: central. Trade-off. Document. Choose per use case.
"""  # noqa: E501

version = "0.0.1"
