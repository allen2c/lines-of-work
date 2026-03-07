"""Knowledge item: system testing workflows."""

title = "Przepływy testów systemowych"

content = """
Testy systemowe weryfikują zachowanie całego systemu jako całości, w warunkach zbliżonych
do produkcji. Obejmują testy funkcjonalne, niefunkcjonalne (wydajność, bezpieczeństwo) oraz
scenariusze awarii. Workflow definiuje kolejność wykonywania, kryteria przejścia i
procedury raportowania.

**Kontekst:** Testy systemowe są ostatnią linią obrony przed wdrożeniem. Muszą być
powtarzalne i wykonywane w środowisku zbliżonym do produkcyjnego.

**Kluczowe działania:**
1) Zdefiniuj środowisko testowe (stage) z konfiguracją zbliżoną do produkcji.
2) Ustal kryteria wejścia (np. wszystkie testy jednostkowe i integracyjne zielone).
3) Automatyzuj wykonywanie w pipeline przed release.
4) Raportuj wyniki do dashboardu i powiadamiaj o niepowodzeniach.
"""

version = "0.0.1"
