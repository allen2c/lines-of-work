"""Knowledge item: timezone and locale testing."""

title = "Testy stref czasowych i ustawień regionalnych"

content = """
Strefy czasowe i ustawienia regionalne (locale) wpływają na formatowanie dat,
liczb i walut. Błędy w tym obszarze prowadzą do nieprawidłowych harmonogramów,
raportów i doświadczeń użytkownika w różnych regionach.

**Kontekst:** Systemy globalne muszą poprawnie obsługiwać UTC, strefy lokalne oraz
przejścia na czas letni/zimowy. Locale określa format daty, separatorów dziesiętnych
i tysięcy.

**Kluczowe działania:**
1) Testuj operacje na datach w kilku strefach (np. UTC, Europe/Warsaw, America/New_York).
2) Weryfikuj formatowanie liczb i walut dla różnych locale.
3) Sprawdź edge cases: północ, zmiana czasu, strefy z przesunięciami niecałkowitymi.
4) Udokumentuj przyjętą strategię przechowywania dat (UTC vs local).
"""

version = "0.0.1"
