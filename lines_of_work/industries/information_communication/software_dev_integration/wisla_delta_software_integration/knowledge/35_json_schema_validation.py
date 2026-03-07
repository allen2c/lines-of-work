title = "Walidacja JSON Schema"

content = """
JSON Schema definiuje strukturę i typy danych JSON. Walidacja na granicy integracji
wykrywa błędy wcześnie, zanim dane trafią do logiki biznesowej.

**Zalety:** Jedna definicja dla dokumentacji, walidacji i generowania kodu. Wersjonowanie
schematów ułatwia ewolucję API.

**Praktyki:** Waliduj zarówno request, jak i response. Używaj strict mode — odrzucaj
nieznane pola. Dla dużych payloadów rozważ walidację strumieniową.
"""  # noqa: E501

version = "0.0.1"
