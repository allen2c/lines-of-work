title = "Identyfikatory korelacji"

content = """
Identyfikatory korelacji (correlation ID) pozwalają śledzić pojedyncze żądanie lub transakcję
przez wiele systemów i usług. Każdy system przekazuje ten sam identyfikator dalej, co umożliwia
skorelowanie logów i metryk w rozproszonym środowisku.

**Generowanie:** Identyfikator powinien być generowany przy pierwszym wejściu żądania do
systemu (np. w API gateway) i przekazywany w nagłówku HTTP (np. X-Correlation-ID) lub w
metadanych wiadomości. Format UUID v4 jest powszechnie stosowany.

**Propagacja:** Każda warstwa integracji musi przekazywać identyfikator do wywołań
zewnętrznych. W REST — nagłówek; w kolejkach — pole w payloadzie lub metadanych.

**Korzyści:** Ułatwia debugowanie, analizę ścieżki żądania i identyfikację wąskich gardeł.
W Delta Wisły stosujemy korelację we wszystkich integracjach produkcyjnych.
"""

version = "0.0.1"
