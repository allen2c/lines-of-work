title = "Mapowanie danych"

content = """
Mapowanie danych to tłumaczenie między schematami źródłowymi a docelowymi. Źle
zaprojektowane mapowanie prowadzi do utraty informacji, błędów biznesowych i
kosztownej konserwacji.

**Mapowanie 1:1:** Pole A → pole B. Proste, ale wymaga obsługi brakujących wartości
i różnych typów (string vs number, formaty dat).

**Mapowanie z transformacją:** Konwersja jednostek, łączenie pól, dzielenie, lookup
w tabelach referencyjnych. Dokumentuj reguły w centralnym repozytorium (np. JSON,
YAML) zamiast hardcodować w kodzie.

**Obsługa null i brakujących pól:** Zdefiniuj domyślne wartości, reguły fallback
lub oznacz rekordy do ręcznej weryfikacji. Unikaj cichego pomijania istotnych pól.

**Walidacja:** Waliduj dane przed i po mapowaniu. Schematy (JSON Schema, Avro)
pomagają wykryć niezgodności wcześnie. Raportuj statystyki mapowania (sukces/błąd).
"""  # noqa: E501

version = "0.0.1"
