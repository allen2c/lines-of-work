title = "System śledzenia i aktualizacje statusu"

content = """
Każda przesyłka jest śledzona przez unikalny numer. Kluczowe zdarzenia (in-gate, sortacja,
out-gate) aktualizują status w systemie i mogą wyzwalać powiadomienia do klienta.

**Zdarzenia rejestrowane w hubie:**
- Przyjęcie w centrum (in-gate)
- Sortacja do korytarza X
- Załadunek na pojazd [numer]
- Wyjazd z centrum (out-gate)

**Synchronizacja:**
Opóźnienie między skanem a aktualizacją w systemie < 5 minut. Rozbieżności
(rejestracja zdarzenia bez fizycznej obecności) są monitorowane i raportowane.
"""  # noqa: E501

version = "0.0.1"
