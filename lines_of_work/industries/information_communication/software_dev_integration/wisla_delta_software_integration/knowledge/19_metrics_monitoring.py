title = "Metryki i monitorowanie integracji"

content = """
Metryki pozwalają wykrywać awarie, spadki wydajności i anomalie. Kluczowe
wskaźniki dla integracji: throughput, latencja, współczynnik błędów, backlog
kolejek.

**Metryki RED (Request):** Rate (zapytania/s), Errors (błędy/s), Duration
(percentyle latencji). Dla kolejek: długość kolejki, czas oczekiwania, dead letter.

**Alerty:** Ustaw progi na percentyle (p99), error rate, dostępność. Unikaj
alertów na pojedyncze błędy — używaj okien czasowych. Runbooks przy alertach.

**Narzędzia:** Prometheus, Grafana, Datadog, CloudWatch. Eksportuj metryki
z aplikacji (Prometheus client, OpenTelemetry).
"""  # noqa: E501

version = "0.0.1"
