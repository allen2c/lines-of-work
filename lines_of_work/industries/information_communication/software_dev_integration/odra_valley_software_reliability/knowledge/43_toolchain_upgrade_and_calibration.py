"""Knowledge item: toolchain upgrade and calibration."""

title = "Aktualizacja i kalibracja toolchainu"

content = """
Narzędzia testowe, frameworki i zależności wymagają regularnych aktualizacji.
Nieaktualne wersje niosą ryzyko luk bezpieczeństwa i niekompatybilności z nowymi
funkcjami systemu.

**Kontekst:** Kalibracja oznacza weryfikację, że narzędzia mierzą to, co zamierzone,
oraz że wyniki są porównywalne między wersjami. Upgrade bez kalibracji może
wprowadzić fałszywe alarmy lub ukryte regresje.

**Kluczowe działania:**
1) Ustal harmonogram aktualizacji (np. kwartalny) dla frameworków testowych.
2) Przeprowadzaj smoke testy po każdej aktualizacji przed mergowaniem.
3) Porównuj wyniki baseline przed i po upgrade, dokumentuj zmiany w metrykach.
4) Zachowaj możliwość rollbacku do poprzedniej wersji w razie problemów.
"""

version = "0.0.1"
