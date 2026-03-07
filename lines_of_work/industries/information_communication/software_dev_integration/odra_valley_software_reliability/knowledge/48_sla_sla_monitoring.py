"""Knowledge item: SLA and SLO monitoring."""

title = "Monitorowanie SLA i SLO"

content = """
SLA (Service Level Agreement) to umowne zobowiązania wobec klientów. SLO (Service
Level Objective) to wewnętrzne cele, które pozwalają spełnić SLA. Monitorowanie
obu wymaga metryk, alertów i procesów reakcji.

**Kontekst:** SLO są zwykle bardziej rygorystyczne niż SLA, aby zapewnić bufor.
Metryki muszą być zdefiniowane jednoznacznie (np. co liczy się jako „downtime”).

**Kluczowe działania:**
1) Zdefiniuj metryki dla każdego SLO (dostępność, latencja, error rate).
2) Skonfiguruj alerty przy zbliżaniu się do progu lub przekroczeniu.
3) Automatyzuj raportowanie SLA dla klientów (jeśli wymagane).
4) Przeprowadzaj regularne przeglądy i dostosowuj cele do zmieniających się potrzeb.
"""

version = "0.0.1"
