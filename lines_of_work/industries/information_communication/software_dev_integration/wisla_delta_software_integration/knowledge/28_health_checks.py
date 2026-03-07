title = "Health checks i readiness probes"

content = """
Health checks informują o stanie integracji. Liveness: czy proces działa. Readiness: czy
może przyjmować ruch (np. połączenia do baz i zewnętrznych usług są gotowe).

**Praktyki:** Endpoint /health zwracający 200 lub 503. Sprawdzaj zależności (bazy, API).
Unikaj ciężkich operacji w health checku — ma być szybki.
"""  # noqa: E501

version = "0.0.1"
