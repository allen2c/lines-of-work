"""Knowledge item: api versioning compatibility."""

title = "Kompatybilność wersjonowania API"

content = """
API ewoluują w czasie. Wersjonowanie i strategia kompatybilności wstecznej decydują
o tym, czy klienci mogą bezpiecznie aktualizować integracje bez przerw w działaniu.

**Kontekst:** Niekompatybilne zmiany API powodują awarie u klientów. Należy stosować
strategię wersjonowania (np. semver, URL versioning) oraz okresy deprecation.

**Kluczowe działania:**
1) Zdefiniuj politykę wersjonowania i kompatybilności wstecznej.
2) Testuj stare i nowe wersje API równolegle przed deprecation.
3) Udokumentuj zmiany breaking i harmonogram migracji klientów.
4) Monitoruj użycie deprecated endpointów przed ich usunięciem.
"""

version = "0.0.1"
