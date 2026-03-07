title = "Idempotencja operacji"

content = """
Operacja jest idempotentna, gdy wielokrotne wykonanie z tymi samymi parametrami
daje ten sam efekt co pojedyncze wykonanie. W integracjach kluczowe przy retry
i odtwarzaniu po awariach.

**Idempotency key:** Klient wysyła unikalny klucz (UUID) z żądaniem. Serwer
zapisuje wynik pierwszego wykonania i przy powtórzeniu zwraca ten sam wynik
bez ponownego przetwarzania. Klucz ważny przez określony czas (np. 24h).

**GET vs POST/PUT:** GET jest z założenia idempotentny. PUT z tym samym URI
i payloadem też. POST zwykle nie — stąd potrzeba jawnego klucza idempotencji.

**Implementacja:** Serwer sprawdza klucz w cache lub DB przed wykonaniem.
Odpowiedź 409 Conflict lub 200 z tym samym body przy duplikacie.
"""  # noqa: E501

version = "0.0.1"
