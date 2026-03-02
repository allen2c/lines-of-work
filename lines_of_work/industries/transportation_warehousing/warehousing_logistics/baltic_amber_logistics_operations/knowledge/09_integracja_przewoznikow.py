title = "Integracja z przewoźnikami i manifestacja"

content = """
Manifestacja to przekazanie danych o przesyłkach przewoźnikowi przed
fizycznym odbiorem. Systemowa integracja skraca czas obsługi i
zmniejsza błędy przy etykietowaniu.

**Formaty integracji:** API REST, EDI, pliki CSV/XML — w zależności
od możliwości przewoźnika. Baltic Amber obsługuje DPD, DHL, InPost,
Omniva (Estonia), Venipak (Litwa, Łotwa).

**Dane wymagane do manifestu:** Numer zamówienia, waga, wymiary,
adres odbioru, numer referencyjny. Dla przesyłek międzynarodowych
— opis towaru w języku angielskim, wartość celna.

**Kolejność:** Kompletacja → pakowanie → ważenie i wymiary →
wpis do systemu → manifestacja → wydruk etykiet → ułożenie na
rampie według przewoźnika. Przesyłki niewymanifestowane nie
opuszczają magazynu.
"""  # noqa: E501

version = "0.0.1"
