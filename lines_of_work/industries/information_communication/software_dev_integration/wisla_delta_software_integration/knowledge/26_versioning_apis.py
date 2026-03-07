title = "Wersjonowanie API"

content = """
API ewoluują. Wersjonowanie pozwala zachować kompatybilność wsteczną. Typowe podejścia:
ścieżka URL (/v1/, /v2/), nagłówek (Accept-Version), parametr zapytania.

**Zasady:** Nie usuwaj od razu starych wersji; ogłoś deprecację z wyprzedzeniem. Dokumentuj
zmiany między wersjami. Dla integracji kluczowe jest planowanie migracji.
"""  # noqa: E501

version = "0.0.1"
