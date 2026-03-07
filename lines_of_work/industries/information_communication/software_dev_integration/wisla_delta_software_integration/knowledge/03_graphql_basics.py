title = "Podstawy GraphQL"

content = """
GraphQL to język zapytań i środowisko wykonawcze dla API, alternatywny do REST.
Pozwala klientom precyzyjnie określać, jakie dane są potrzebne, redukując nadmiar i
liczbę round-tripów.

**Zapytania i mutacje:** Zapytania (queries) służą do odczytu danych; mutacje (mutations)
do modyfikacji. Subskrypcje (subscriptions) umożliwiają aktualizacje w czasie rzeczywistym
przez WebSocket.

**Schemat:** GraphQL jest silnie typowany. Schemat definiuje typy, pola, argumenty i
relacje. Walidacja odbywa się przed wykonaniem.

**Integracja z systemami legacy:** GraphQL może pełnić rolę warstwy agregującej nad
wieloma backendami REST lub bazami danych. Resolvery mapują pola na wywołania zewnętrzne.

**Uwagi:** GraphQL wymaga więcej infrastruktury (parsowanie, walidacja, N+1 queries).
Dobrze sprawdza się przy złożonych modelach danych i klientach mobilnych.
"""  # noqa: E501

version = "0.0.1"
