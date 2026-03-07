"""Knowledge item: integration testing protocols."""

title = "Protokoły testów integracyjnych"

content = """
Protokoły testów integracyjnych definiują, jak testować interakcje między komponentami:
API, bazy danych, kolejki, zewnętrzne serwisy. Testy muszą używać izolowanych środowisk
(testcontainers, mock servers) i czyścić dane między uruchomieniami.

**Kontekst:** Testy integracyjne wykrywają błędy na granicach systemu, które testy
jednostkowe pomijają. Wymagają starannego zarządzania stanem i zależnościami.

**Kluczowe działania:**
1) Zdefiniuj scope: które integracje testować w CI, które w stage.
2) Używaj testcontainers lub równoważnych narzędzi dla spójności z produkcją.
3) Implementuj setup/teardown zapewniający czysty stan.
4) Monitoruj czas wykonania; optymalizuj lub przenoś wolne testy do osobnego pipeline.
"""

version = "0.0.1"
