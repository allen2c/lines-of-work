title = "Rozproszone śledzenie (Distributed Tracing)"

content = """
Tracing śledzi pojedyncze żądanie przez wiele serwisów. Każda operacja ma
trace ID i span ID. Spany tworzą drzewo — widać, gdzie czas został spędzony
i które wywołania zawiodły.

**OpenTelemetry:** Standard de facto. Instrumentacja bibliotek (HTTP, Kafka,
DB). Eksport do Jaeger, Zipkin, Tempo, X-Ray.

**Kontekst propagacji:** Trace ID i Span ID przekazywane w nagłówkach HTTP
(traceparent) lub w metadanych wiadomości. Wszystkie serwisy muszą propagować
kontekst.

**Korzyści:** Identyfikacja wąskich gardeł, analiza opóźnień w łańcuchu,
szybsza diagnoza incydentów. Korelacja z logami przez trace ID.
"""  # noqa: E501

version = "0.0.1"
