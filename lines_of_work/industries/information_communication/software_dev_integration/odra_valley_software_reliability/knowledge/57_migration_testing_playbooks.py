"""Knowledge item: migration testing playbooks."""

title = "Playbooki testowania migracji"

content = """
Migracje danych, schematów lub infrastruktury niosą wysokie ryzyko. Playbooki
testowania migracji definiują kroki weryfikacji przed, w trakcie i po migracji.

**Kontekst:** Nieudana migracja może spowodować utratę danych lub długotrwałą
niedostępność. Playbook powinien obejmować rollback, weryfikację integralności
oraz procedury awaryjne.

**Kluczowe działania:**
1) Stwórz playbook dla każdego typu migracji (DB, API, infrastruktura).
2) Uwzględnij testy przed migracją (dry-run) i po migracji (sanity check).
3) Zdefiniuj kryteria sukcesu i warunki rollbacku.
4) Przeprowadź retrospektywę po każdej migracji.
"""

version = "0.0.1"
