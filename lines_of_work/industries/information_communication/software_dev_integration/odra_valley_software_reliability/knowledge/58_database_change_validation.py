"""Knowledge item: database change validation."""

title = "Walidacja zmian w bazie danych"

content = """
Zmiany schematu bazy danych wymagają szczególnej uwagi ze względu na ryzyko utraty
danych i niekompatybilności wstecznej. Migracje muszą być testowane w środowiskach
zbliżonych do produkcji.

**Kontekst:** Błędy w migracjach mogą być trudne do cofnięcia i mogą wpłynąć na
wiele usług. Należy weryfikować zarówno poprawność migracji, jak i zachowanie
aplikacji po zmianie.

**Kluczowe działania:**
1) Testuj migracje na kopii danych produkcyjnych (anonimizowanych).
2) Weryfikuj rollback migracji przed wdrożeniem.
3) Sprawdź kompatybilność wsteczną API i zapytań.
4) Udokumentuj zależności między migracjami a wersjami aplikacji.
"""

version = "0.0.1"
