title = "Obsługa błędów w integracjach"

content = """
Solidna obsługa błędów w integracjach zapobiega kaskadowym awariom i utracie danych.
Kluczowe jest rozróżnienie błędów przejściowych od trwałych oraz właściwa reakcja.

**Błędy przejściowe:** Timeout, 503 Service Unavailable, rate limit (429). Strategia:
retry z exponential backoff, ograniczona liczba prób. Nie blokuj całego pipeline'u.

**Błędy trwałe:** 400 Bad Request, 404 Not Found, błędy walidacji. Retry nie pomoże.
Loguj, raportuj, kieruj do dead-letter lub kwarantanny. Wymagają interwencji człowieka.

**Circuit breaker:** Przy powtarzających się awariach zewnętrznego systemu zatrzymaj
wywołania na określony czas (open state), potem spróbuj ponownie (half-open).
Zapobiega przeciążeniu i marnowaniu zasobów.

**Idempotentność:** Przy retry upewnij się, że operacja jest idempotentna lub użyj
kluczy idempotentności, aby uniknąć duplikatów.
"""  # noqa: E501

version = "0.0.1"
