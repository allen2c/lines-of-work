"""Knowledge item: telemetry for quality."""

title = "Telemetria na potrzeby jakości"

content = """
Telemetria (metryki, zdarzenia) dostarcza danych do oceny jakości i niezawodności w
czasie rzeczywistym. Wskaźniki takie jak latency, error rate, throughput są niezbędne
do podejmowania decyzji o wdrożeniach.

**Kontekst:** Metryki muszą być zdefiniowane przed wdrożeniem, aby móc porównać stan
przed i po. SLO opierają się na tych samych metrykach, co alerty.

**Kluczowe działania:**
1) Zdefiniuj metryki biznesowe i techniczne (latency p50/p95/p99, error rate, RPS).
2) Włącz instrumentację w kluczowych punktach (endpointy, baza, zewnętrzne API).
3) Skonfiguruj dashboardy z baseline przed wdrożeniem.
4) Użyj metryk do weryfikacji post-release: czy wskaźniki są w akceptowalnym zakresie.
5) Powiąż metryki z error budgetem i SLO.
"""

version = "0.0.1"
