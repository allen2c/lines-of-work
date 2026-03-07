title = "Wzorce webhooków"

content = """
Webhooki umożliwiają integrację opartą na zdarzeniach: system zewnętrzny wysyła HTTP
POST do Twojego endpointu, gdy wystąpi zdarzenie (np. nowe zamówienie, zmiana statusu).

**Implementacja odbioru:** Endpoint musi być idempotentny (ten sam payload może przyjść
wielokrotnie). Weryfikuj podpis (HMAC) lub token w nagłówku, aby potwierdzić autentyczność.
Odpowiedz 2xx szybko (w ciągu kilku sekund), przetwarzaj asynchronicznie.

**Implementacja wysyłania:** Używaj retry z exponential backoff przy niepowodzeniach.
Przechowuj historię dostaw do audytu. Rozważ dead-letter queue dla nieudanych prób.

**Bezpieczeństwo:** Nigdy nie ufaj payloadowi bez weryfikacji. Używaj HTTPS. Ogranicz
rozmiar payloadu. Rozważ whitelistę adresów IP nadawcy.

**Alternatywy:** Dla wysokiej przepustowości rozważ message queue zamiast webhooków
bezpośrednich — webhooki są prostsze, ale mniej odporne na przeciążenie.
"""  # noqa: E501

version = "0.0.1"
