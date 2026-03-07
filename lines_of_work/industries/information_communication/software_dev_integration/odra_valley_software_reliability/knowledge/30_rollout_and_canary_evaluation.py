"""Knowledge item: rollout and canary evaluation."""

title = "Wdrożenie i ocena canary"

content = """
Canary deployment polega na kierowaniu niewielkiego procentu ruchu na nową wersję,
aby wykryć problemy zanim wpłyną na wszystkich użytkowników. Ocena canary wymaga
zdefiniowanych kryteriów sukcesu i porażki.

**Kontekst:** Bez jasnych kryteriów zespół nie wie, kiedy przerwać rollout lub
kontynuować. Metryki (error rate, latency) muszą być porównywane z baseline.

**Kluczowe działania:**
1) Zdefiniuj kryteria sukcesu (np. error rate < baseline + 0.1%, latency p99 < 2x baseline).
2) Zdefiniuj kryteria porażki (np. error rate > 2%, wzrost latency > 50%).
3) Ustal czas obserwacji przed zwiększeniem procentu ruchu.
4) Skonfiguruj automatyczne rollback przy przekroczeniu kryteriów porażki.
5) Udokumentuj procedurę ręcznego rollbacku i komunikacji.
"""

version = "0.0.1"
