title = "Podstawy projektowania API"

content = """
Projektowanie API to fundament integracji systemów. Dobrze zaprojektowane API ułatwia
łączenie aplikacji, redukuje koszty utrzymania i zapewnia spójność danych między systemami.

**Zasady projektowania:** API powinno być spójne, przewidywalne i dobrze udokumentowane.
Używaj standardowych konwencji HTTP (GET do odczytu, POST do tworzenia, PUT/PATCH do
aktualizacji, DELETE do usuwania). Nazewnictwo zasobów powinno być rzeczownikowe i w liczbie
mnogiej (np. /klienci, /zamowienia).

**Wersjonowanie:** Wprowadź wersjonowanie od początku — w ścieżce (/v1/klienci) lub nagłówkach.
Unikaj łamania kompatybilności wstecznej; nowe pola dodawaj opcjonalnie.

**Obsługa błędów:** Zwracaj spójne kody HTTP i struktury błędów. Używaj 4xx dla błędów
klienta, 5xx dla błędów serwera. Dołącz czytelne komunikaty i kody błędów do debugowania.
"""  # noqa: E501

version = "0.0.1"
