"""Knowledge item: feature flag verification."""

title = "Weryfikacja feature flagów"

content = """
Feature flagi umożliwiają stopniowe wdrażanie funkcji i szybkie wycofanie w razie
problemów. Należy weryfikować, że flagi działają poprawnie i nie wprowadzają
nieoczekiwanych ścieżek kodu.

**Kontekst:** Błędna konfiguracja flag może ujawnić niedokończone funkcje lub ukryć
krytyczne ścieżki. Testy muszą obejmować różne kombinacje flag.

**Kluczowe działania:**
1) Zdefiniuj macierz testową: funkcja vs wartość flagi (on/off/default).
2) Testuj ścieżki z flagą włączoną i wyłączoną dla każdej funkcji krytycznej.
3) Weryfikuj fallback: co się dzieje, gdy serwis flag jest niedostępny.
4) Sprawdź, że flagi nie eksponują danych testowych ani debugowych w produkcji.
5) Udokumentuj politykę życia flag (kiedy usunąć po pełnym rollout).
"""

version = "0.0.1"
