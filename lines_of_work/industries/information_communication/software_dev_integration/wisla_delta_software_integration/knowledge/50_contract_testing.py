title = "Testowanie kontraktów"

content = """
Testowanie kontraktów weryfikuje, że konsument i dostawca API są zgodni co do formatu
komunikacji. Zamiast testów end-to-end, które wymagają wszystkich systemów, testy
kontraktów sprawdzają oczekiwania w izolacji.

**Pact i podobne narzędzia:** Pact pozwala konsumentowi zdefiniować oczekiwany kontrakt;
dostawca weryfikuje, że go spełnia. Kontrakt jest zapisywany i wersjonowany.

**Korzyści:** Wykrywa niekompatybilności przed wdrożeniem. Umożliwia niezależne
wdrażanie usług. Redukuje ryzyko regresji przy zmianach API.

**Praktyki Delta Wisły:** Wymagamy testów kontraktów dla wszystkich publicznych
integracji. Kontrakty są przechowywane w repozytorium i aktualizowane przy zmianach API.
"""

version = "0.0.1"
