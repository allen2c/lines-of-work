title = "Konwencje REST"

content = """
REST (Representational State Transfer) to dominujący styl architektury dla API opartych
na HTTP. Zrozumienie konwencji REST jest niezbędne przy integracji systemów korporacyjnych.

**Zasoby i reprezentacje:** Każda encja biznesowa jest zasobem identyfikowanym przez URI.
Klient operuje na reprezentacjach (np. JSON, XML). Stan jest bezserwerowy — każdy request
zawiera pełny kontekst.

**Metody HTTP:** GET (idempotentny odczyt), POST (tworzenie), PUT (pełna zamiana),
PATCH (częściowa aktualizacja), DELETE (usunięcie). Używaj metod zgodnie z semantyką.

**Kody odpowiedzi:** 200 OK, 201 Created, 204 No Content, 400 Bad Request, 401 Unauthorized,
403 Forbidden, 404 Not Found, 409 Conflict, 422 Unprocessable Entity, 500 Internal Server Error.

**HATEOAS (opcjonalnie):** Odpowiedzi mogą zawierać linki do powiązanych zasobów,
ułatwiając klientowi nawigację bez znajomości stałych ścieżek.
"""  # noqa: E501

version = "0.0.1"
