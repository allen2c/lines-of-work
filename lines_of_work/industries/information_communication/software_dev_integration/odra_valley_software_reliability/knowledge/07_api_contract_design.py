"""Knowledge item: API contract design."""

title = "Projektowanie kontraktów API"

content = """
Kontrakty API definiują oczekiwane zachowanie interfejsów między usługami. Dobrze zaprojektowane
kontrakty zmniejszają ryzyko niekompatybilności przy zmianach wersji i ułatwiają testowanie
integracji.

**Kontekst:** W architekturze mikroserwisów każda zmiana API może wpłynąć na wiele konsumentów.
Kontrakty powinny być wersjonowane, udokumentowane i testowane automatycznie (contract testing).

**Kluczowe działania:**
1) Użyj formatów takich jak OpenAPI lub AsyncAPI do definiowania kontraktów.
2) Wdróż contract testing (np. Pact, Spring Cloud Contract) w pipeline.
3) Zdefiniuj politykę wersjonowania i deprecacji.
4) Udokumentuj zachowanie przy błędach i limitach (rate limiting, timeouts).
5) Przeglądaj kontrakty przy każdej zmianie API.
"""

version = "0.0.1"
