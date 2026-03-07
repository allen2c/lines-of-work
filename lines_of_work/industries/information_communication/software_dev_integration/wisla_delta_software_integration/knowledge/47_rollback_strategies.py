title = "Strategie wycofywania integracji"

content = """
Przy wdrożeniu nowej wersji integracji przygotuj plan rollbacku. Zachowaj
kompatybilność wsteczną przez okres przejściowy. Feature flags pozwalają
wyłączyć nową ścieżkę bez redeployu. Wersjonowanie API umożliwia równoległe
działanie starej i nowej wersji. Monitoruj metryki po wdrożeniu — automatyczny
rollback przy przekroczeniu progu błędów.

**Zasada:** Każde wdrożenie integracji musi mieć zdefiniowany warunek rollbacku
i procedurę przywrócenia stanu poprzedniego.
"""  # noqa: E501

version = "0.0.1"
