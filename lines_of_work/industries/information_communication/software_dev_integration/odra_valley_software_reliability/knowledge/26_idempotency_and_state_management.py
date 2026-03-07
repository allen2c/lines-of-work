"""Knowledge item: idempotency and state management."""

title = "Idempotencja i zarządzanie stanem"

content = """
Operacje idempotentne zwracają ten sam wynik przy wielokrotnym wywołaniu z tymi samymi
danych wejściowych. W środowiskach rozproszonych retry i duplikaty są nieuniknione;
idempotencja zapobiega podwójnemu przetwarzaniu.

**Kontekst:** Klient może wysłać żądanie wielokrotnie z powodu timeoutu lub awarii sieci.
Serwer musi rozpoznać duplikat i zwrócić poprzedni wynik zamiast wykonywać operację ponownie.

**Kluczowe działania:**
1) Zdefiniuj klucze idempotencji (np. Idempotency-Key w nagłówku) dla operacji mutujących.
2) Przechowuj wyniki operacji idempotentnych przez określony czas (TTL).
3) Testuj retry z tym samym kluczem: odpowiedź powinna być identyczna.
4) Weryfikuj, że operacje niezmieniające stan (GET) są z natury idempotentne.
5) Udokumentuj politykę TTL i czyszczenia kluczy idempotencji.
"""

version = "0.0.1"
