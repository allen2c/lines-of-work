"""Knowledge item: input validation and sanitization."""

title = "Walidacja i sanityzacja danych wejściowych"

content = """
Niezwalidowane dane wejściowe są główną przyczyną luk bezpieczeństwa (injection, XSS) oraz
błędów biznesowych. Każdy punkt wejścia (API, formularz, plik) wymaga walidacji i sanityzacji.

**Kontekst:** W usługach rozproszonych dane przechodzą przez wiele warstw. Walidacja musi
być spójna na granicach systemu oraz wewnątrz domeny.

**Kluczowe działania:**
1) Zdefiniuj schematy walidacji (np. JSON Schema, Pydantic) dla wszystkich endpointów.
2) Testuj edge cases: puste wartości, bardzo długie stringi, znaki specjalne, Unicode.
3) Weryfikuj sanityzację przed zapisem do bazy i przed wyświetleniem użytkownikowi.
4) Sprawdź obsługę błędów walidacji (kody HTTP, komunikaty).
5) Udokumentuj dozwolone zakresy i formaty dla każdego pola.
"""

version = "0.0.1"
