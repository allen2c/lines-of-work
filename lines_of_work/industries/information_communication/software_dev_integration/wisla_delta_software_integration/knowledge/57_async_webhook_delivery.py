title = "Dostarczanie webhooków asynchronicznych"

content = """
Webhooki są wywoływane asynchronicznie przez dostawcę — odbiorca musi być gotowy na
opóźnienia, ponowne dostawy i nieuporządkowanie. Projektowanie odbiornika wymaga
uwzględnienia tych cech.

**Idempotencja:** Ten sam webhook może być dostarczony wielokrotnie (retry po timeout).
Odbiorca musi rozpoznać duplikaty (np. po idempotency key) i zwrócić 200 bez
powtórnego przetwarzania.

**Szybka odpowiedź:** Endpoint webhooka powinien zwrócić 2xx w ciągu kilku sekund.
Ciężkie przetwarzanie — w tle, po zakolejkowaniu. Timeout po stronie nadawcy
(najczęściej 5–30 s) wymusza tę praktykę.

**Delta Wisła:** Wszystkie odbiorniki webhooków: walidacja podpisu, idempotencja,
kolejka do asynchronicznego przetwarzania, retry z exponential backoff przy błędach.
"""

version = "0.0.1"
