"""Knowledge item: localization and encoding tests."""

title = "Testy lokalizacji i kodowania"

content = """
Lokalizacja (l10n) i obsługa różnych kodowań (UTF-8, ISO-8859 itd.) są istotne dla
systemów obsługujących użytkowników wielojęzycznych. Błędy w tym obszarze powodują
uszkodzenie danych, błędne wyświetlanie lub awarie parsowania.

**Kontekst:** Polskie znaki diakrytyczne, znaki CJK, RTL oraz mieszane encodings
w jednym systemie wymagają świadomego testowania. Baza danych, API i warstwa
prezentacji muszą być spójne.

**Kluczowe działania:**
1) Testuj krytyczne ścieżki z danymi w docelowych językach i encodings.
2) Weryfikuj poprawność round-trip (zapis–odczyt) dla znaków specjalnych.
3) Sprawdź obsługę pustych stringów, null i edge cases w parsowaniu.
4) Udokumentuj obsługiwane encodings i języki w specyfikacji.
"""

version = "0.0.1"
