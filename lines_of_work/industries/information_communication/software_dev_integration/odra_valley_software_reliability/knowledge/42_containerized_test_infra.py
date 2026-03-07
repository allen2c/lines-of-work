"""Knowledge item: containerized test infrastructure."""

title = "Konteneryzowana infrastruktura testowa"

content = """
Kontenery (Docker, Kubernetes) umożliwiają izolowane, powtarzalne środowiska testowe.
Infrastruktura testowa oparta na kontenerach przyspiesza CI/CD i redukuje flakiness
związany z różnicami między maszynami.

**Kontekst:** Testy muszą uruchamiać się w środowisku zbliżonym do produkcji. Kontenery
zapewniają deterministyczne buildy i łatwe skalowanie równoległych przebiegów.

**Kluczowe działania:**
1) Użyj Dockerfile'ów lub Helm charts zdefiniowanych dla środowisk testowych.
2) Zarządzaj cyklem życia kontenerów (start, stop, cleanup) w pipeline'ach.
3) Monitoruj zużycie zasobów i czas uruchomienia, aby uniknąć timeoutów.
4) Udokumentuj wymagania sieciowe i zależności między serwisami w klastrze.
"""

version = "0.0.1"
