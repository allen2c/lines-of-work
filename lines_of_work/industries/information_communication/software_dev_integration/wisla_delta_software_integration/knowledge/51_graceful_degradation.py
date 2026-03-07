title = "Graceful degradation"

content = """
Graceful degradation oznacza, że system kontynuuje działanie z ograniczoną funkcjonalnością,
gdy zależna usługa jest niedostępna, zamiast całkowicie się wyłączać. Kluczowe dla
niezawodności integracji.

**Strategie:** Cache ostatnich odpowiedzi, tryb offline z kolejką do późniejszej synchronizacji,
fallback do uproszczonej wersji danych lub domyślnych wartości. Komunikowanie użytkownikowi
ograniczeń zamiast błędu.

**Implementacja:** Circuit breaker, timeouty i retry z backoff zapobiegają kaskadowym
awariom. Monitorowanie stanu zależności pozwala na proaktywne przełączanie w tryb
degradacji.

**Delta Wisła:** Dla krytycznych integracji definiujemy minimalny zestaw funkcji w trybie
degradacji i procedury przywracania pełnej funkcjonalności.
"""

version = "0.0.1"
