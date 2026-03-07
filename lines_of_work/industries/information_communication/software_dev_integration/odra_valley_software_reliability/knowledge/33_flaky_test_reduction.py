"""Knowledge item: flaky test reduction."""

title = "Redukcja testów flaky"

content = """
Testy flaky to takie, które czasami przechodzą, a czasami nie, przy tej samej wersji kodu.
Osłabiają zaufanie do zestawu testowego, opóźniają pipeline i generują fałszywe alarmy.
Redukcja flakiness jest priorytetem dla utrzymania jakości procesu.

**Kontekst:** Przyczyny flakiness obejmują: zależności od czasu, nieokreślona kolejność
wykonania, współdzielony stan, zewnętrzne zależności sieciowe, race conditions.
Każda przyczyna wymaga innego podejścia naprawczego.

**Kluczowe działania:**
1) Identyfikuj testy flaky przez analizę historii uruchomień i oznaczenia w CI.
2) Izoluj przyczynę: logi, powtórzenia, mockowanie zewnętrznych zależności.
3) Napraw lub usuń: preferuj naprawę, usuwaj tylko gdy test nie ma wartości.
4) Wprowadź politykę: test flaky po N niepowodzeniach jest blokowany lub quarantined.
5) Przeglądaj quarantined testy co sprint i decyduj o naprawie lub usunięciu.
"""

version = "0.0.1"
