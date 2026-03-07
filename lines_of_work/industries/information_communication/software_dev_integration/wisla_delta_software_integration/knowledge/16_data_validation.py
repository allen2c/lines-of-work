title = "Walidacja danych w integracjach"

content = """
Walidacja na granicach integracji zapobiega propagacji błędnych danych. Waliduj
zarówno dane wejściowe (od systemów zewnętrznych), jak i wyjściowe (przed
wysłaniem).

**Typy walidacji:** Format (JSON Schema, XSD), zakres wartości, wymagane pola,
unikalność, relacje między polami. Walidacja biznesowa (np. NIP, PESEL w Polsce).

**Moment walidacji:** Fail fast przy wejściu — odrzuć nieprawidłowe dane zanim
trafią do przetwarzania. Zwróć czytelny błąd 400 z opisem problemu. Nie
przechowuj nieprawidłowych rekordów bez oznaczenia.

**Narzędzia:** JSON Schema, Pydantic, Cerberus. W ETL — Great Expectations,
dbt tests.
"""  # noqa: E501

version = "0.0.1"
