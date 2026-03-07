"""Knowledge item: dependency risk management."""

title = "Zarządzanie ryzykiem zależności"

content = """
Zarządzanie ryzykiem zależności obejmuje identyfikację, ocenę i mitygację zagrożeń związanych
z bibliotekami, usługami zewnętrznymi oraz infrastrukturą. Zależności są częstym źródłem
awarii i luk bezpieczeństwa.

**Kontekst:** Każda zależność wprowadza ryzyko: awaria dostawcy, zmiana API, podatność
bezpieczeństwa, niekompatybilność wersji. Należy mieć procedury monitorowania i aktualizacji.

**Kluczowe działania:**
1) Utrzymuj rejestr zależności z wersjami i właścicielami.
2) Wdróż skanowanie podatności (np. Dependabot, Snyk) w CI/CD.
3) Zdefiniuj politykę aktualizacji (critical vs. optional).
4) Dla usług zewnętrznych: ustal SLA, monitoruj dostępność, zaplanuj fallback.
5) Przeglądaj zależności przy każdym większym release.
"""

version = "0.0.1"
