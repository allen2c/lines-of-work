title = "Testowanie integracji"

content = """
Testy integracyjne weryfikują współdziałanie systemów. Poziomy: jednostkowe (mock),
kontraktowe (Pact, OpenAPI), end-to-end (środowisko testowe).

**Kontraktowe:** Zapewniają zgodność API bez uruchamiania wszystkich serwisów.
Consumer i provider testują niezależnie przeciw wspólnej specyfikacji.

**E2E:** Pełny przepływ z prawdziwymi lub sandbox API. Wolniejsze, wymagają
środowiska. Używaj do krytycznych ścieżek i przed release.
"""  # noqa: E501

version = "0.0.1"
