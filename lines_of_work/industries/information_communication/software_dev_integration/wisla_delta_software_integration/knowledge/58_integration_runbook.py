title = "Runbook dla integracji"

content = """
Każda integracja produkcyjna powinna mieć runbook — dokument operacyjny z procedurami
diagnostyki, naprawy i eskalacji. Runbook skraca czas reakcji przy awariach i ułatwia
on-call.

**Zawartość:** Opis integracji i zależności, metryki kluczowe i progi alertów, typowe
objawy awarii i przyczyny, kroki diagnostyczne (sprawdzenie logów, health check,
status zewnętrznego API), procedury naprawy (restart, rollback, przełączenie na
fallback), kontakty eskalacyjne i warunki eskalacji.

**Aktualizacja:** Runbook jest aktualizowany przy każdej istotnej zmianie integracji.
Przegląd kwartalny. W Delta Wisły runbooki są przechowywane w repozytorium obok kodu
integracji.
"""

version = "0.0.1"
