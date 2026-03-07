title = "Ograniczanie częstotliwości zapytań (Rate Limiting)"

content = """
Rate limiting chroni systemy przed przeciążeniem i nadużyciami. W integracjach API
klient musi respektować limity serwera i implementować mechanizmy backoff przy
osiągnięciu progu.

**Typy limitów:** Limit na okno czasowe (np. 100 zapytań/minutę), limit burst
(dopuszczalne krótkotrwałe przekroczenie), limit per-user lub per-klucz. Nagłówki
Retry-After i X-RateLimit-Remaining informują klienta o dostępnej pojemności.

**Strategie klienta:** Buforowanie zapytań, kolejkowanie, exponential backoff
przy 429. Priorytetyzacja krytycznych operacji. Cache'owanie odpowiedzi tam, gdzie
możliwe, aby zmniejszyć liczbę wywołań.

**GDPR i RODO:** W kontekście UE limity nie mogą nieuzasadnione blokować dostępu
do danych osobowych. Należy udokumentować uzasadnienie limitów.
"""  # noqa: E501

version = "0.0.1"
