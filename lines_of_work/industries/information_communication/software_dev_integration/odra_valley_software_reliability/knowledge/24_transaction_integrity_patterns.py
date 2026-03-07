"""Knowledge item: transaction integrity patterns."""

title = "Wzorce integralności transakcji"

content = """
Transakcje muszą być atomowe, spójne, izolowane i trwałe (ACID). W systemach rozproszonych
osiągnięcie tego wymaga wzorców takich jak saga, outbox lub two-phase commit.

**Kontekst:** Niepełne transakcje prowadzą do niespójności danych (np. płatność zrealizowana,
ale zamówienie nie utworzone). Należy projektować kompensacje i idempotencję.

**Kluczowe działania:**
1) Zidentyfikuj transakcje rozproszone i ich granice.
2) Zdefiniuj kroki kompensacji dla każdego kroku saga.
3) Weryfikuj izolację: czy równoległe transakcje nie powodują lost updates.
4) Testuj scenariusze awarii w trakcie transakcji (timeout, crash).
5) Udokumentuj wzorce użyte w systemie i ich ograniczenia.
"""

version = "0.0.1"
