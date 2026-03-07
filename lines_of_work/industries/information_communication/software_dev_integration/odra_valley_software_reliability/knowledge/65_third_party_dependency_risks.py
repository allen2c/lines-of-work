"""Knowledge item: third party dependency risks."""

title = "Ryzyka zależności stron trzecich"

content = """
Zależności od bibliotek i usług zewnętrznych wprowadzają ryzyko awarii, luk bezpieczeństwa
i niekompatybilności. Zespół niezawodności musi identyfikować krytyczne zależności i planować
testy oraz strategie łagodzenia.

**Kontekst:** Pojedyncza awaria dostawcy API lub podatność w bibliotece może sparaliżować
system. Należy mapować zależności, monitorować ich stan i mieć plan awaryjny.

**Kluczowe działania:**
1) Utwórz inwentarz krytycznych zależności z poziomem ryzyka.
2) Monitoruj CVE i advisories dla używanych bibliotek.
3) Testuj degradację i fallback przy niedostępności zewnętrznych usług.
4) Określ strategię aktualizacji i okna maintenance.
"""

version = "0.0.1"
