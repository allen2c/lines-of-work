"""Knowledge item: authentication and authorization tests."""

title = "Testy uwierzytelniania i autoryzacji"

content = """
Testy uwierzytelniania i autoryzacji weryfikują, czy system poprawnie identyfikuje użytkowników
oraz czy przyznaje dostęp do zasobów zgodnie z polityką. Błędy w tej warstwie prowadzą do
wycieków danych lub nieautoryzowanego dostępu.

**Kontekst:** W usługach API-driven każdy endpoint musi być chroniony. Należy testować scenariusze
z tokenami wygasłymi, nieprawidłowymi, brakującymi oraz z różnymi rolami użytkowników.

**Kluczowe działania:**
1) Testuj wszystkie ścieżki krytyczne z tokenem JWT/OAuth oraz bez tokena.
2) Weryfikuj granice ról: czy użytkownik A nie ma dostępu do zasobów użytkownika B.
3) Sprawdź obsługę wygasłych i odwołanych tokenów.
4) Testuj rate limiting i blokowanie po nieudanych próbach logowania.
5) Udokumentuj macierz dostępu: rola vs zasób vs dozwolone operacje.
"""

version = "0.0.1"
