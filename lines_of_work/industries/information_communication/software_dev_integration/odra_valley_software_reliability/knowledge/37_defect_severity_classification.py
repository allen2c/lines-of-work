"""Knowledge item: defect severity classification."""

title = "Klasyfikacja ważności defektów"

content = """
Klasyfikacja ważności (severity) defektów pozwala priorytetyzować naprawy i ustalać
kryteria blokowania wydań. Niespójna klasyfikacja prowadzi do chaosu w backlogu
i ryzyka wypuszczenia krytycznych błędów.

**Kontekst:** Severity powinno odzwierciedlać wpływ na użytkownika i biznes, nie
trudność naprawy. Typowe skale: Critical (system niedostępny), High (kluczowa
funkcja nie działa), Medium (degradacja), Low (drobne), Trivial (kosmetyka).

**Kluczowe działania:**
1) Zdefiniuj kryteria dla każdego poziomu severity w dokumentacji zespołowej.
2) Użyj severity do ustalenia SLA na naprawę (np. Critical: 24 h, High: 1 tydzień).
3) Powiąż severity z bramami jakości: np. brak otwartych Critical/High przed release.
4) Przeglądaj klasyfikacje przy eskalacji i koryguj w razie potrzeby.
5) Raportuj trendy severity w przeglądach jakości.
"""

version = "0.0.1"
