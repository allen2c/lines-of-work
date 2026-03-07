title = "Rola API Gateway w integracji"

content = """
API Gateway stanowi pojedynczy punkt wejścia dla żądań zewnętrznych. Centralizuje
autentykację, rate limiting, routing i transformację.

**Dla integracji:** Gateway może agregować wiele backendów, tłumaczyć protokoły,
cache'ować odpowiedzi. Ułatwia ewolucję — zmiana backendu bez zmiany kontraktu zewnętrznego.

**Uwagi:** Gateway to dodatkowa warstwa — opóźnienie, punkt awarii. Używaj gdy
korzyści (bezpieczeństwo, agregacja) przewyższają koszty.
"""  # noqa: E501

version = "0.0.1"
