title = "Wzorce paginacji"

content = """
Integracje często wymagają pobierania dużych zbiorów danych. Paginacja ogranicza
obciążenie i zużycie pamięci. Trzy główne podejścia:

**Offset/limit:** Klasyczne `?offset=100&limit=50`. Proste, ale wolne przy dużych
offsetach (skanowanie). Nadaje się do małych zbiorów i eksportów.

**Cursor-based:** Token kursora z ostatniego elementu. Skalowalne, spójne przy
zmieniających się danych. Preferowane dla strumieni i dużych zbiorów.

**Keyset:** Sortowanie po unikalnym kluczu z warunkiem `WHERE id > last_id`.
Wydajne, wymaga indeksu. Używane w bazach i API wewnętrznych.
"""  # noqa: E501

version = "0.0.1"
