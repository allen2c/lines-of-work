title = "Reguły transformacji danych"

content = """
Transformacja danych między systemami wymaga jasnych reguł mapowania, walidacji i
obsługi wartości specjalnych. Nieudokumentowane lub niekonsekwentne transformacje
powodują błędy trudne do zlokalizowania.

**Dokumentacja:** Dla każdego pola: źródło, cel, reguła transformacji (np. konwersja
jednostek, format daty), wartość domyślna przy braku danych, obsługa null/empty.

**Typowe transformacje:** Konwersja kodów (np. ISO 3166), normalizacja formatów
(telefon, adres), agregacja lub rozdzielenie pól, enkoding znaków (UTF-8).

**Narzędzia:** W Delta Wisły używamy deklaratywnych mapowań (YAML/JSON) gdzie to
możliwe, z walidacją schematu. Złożone logiki — w kodzie z testami jednostkowymi.
"""

version = "0.0.1"
