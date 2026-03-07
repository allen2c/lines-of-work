title = "Dobre praktyki logowania w integracjach"

content = """
Logi w integracjach muszą umożliwiać debugowanie przepływów między systemami
i analizę incydentów. Strukturyzowane logi (JSON) ułatwiają agregację i wyszukiwanie.

**Co logować:** Request ID (propagowany przez wszystkie systemy), timestamp,
źródło i cel, czas trwania, status. Dla błędów — stack trace, payload (bez
danych wrażliwych). Nie loguj haseł, tokenów, pełnych numerów kart.

**Poziomy:** DEBUG dla payloadów w dev, INFO dla udanych operacji, WARN dla
retry, ERROR dla awarii. W produkcji zazwyczaj INFO lub WARN.

**Korelacja:** Używaj correlation ID w nagłówkach (X-Request-ID, X-Correlation-ID).
Przekazuj go do downstreamów. Umożliwia śledzenie pojedynczego żądania przez
cały łańcuch.
"""  # noqa: E501

version = "0.0.1"
