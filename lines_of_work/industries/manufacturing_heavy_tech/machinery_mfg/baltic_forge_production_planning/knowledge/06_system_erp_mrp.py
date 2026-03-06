title = "System ERP i moduł MRP"

content = """
ERP (Enterprise Resource Planning) integruje dane z produkcji, magazynu, zaopatrzenia
i sprzedaży. Moduł MRP (Material Requirements Planning) oblicza zapotrzebowanie
na materiały i sugeruje harmonogram produkcji.

**Dane wejściowe MRP:** Plan produkcji (MPS), BOM, stany magazynowe, lead times,
otwarte zlecenia. Jakość danych decyduje o jakości planu.

**Wyniki:** Zlecenia produkcyjne, zapotrzebowanie na zakupy, sugestie terminów.
Planista nie wykonuje MRP ślepo — weryfikuje i koryguje w kontekście realnych
ograniczeń (awarie, pilne zmiany).

**Integracja z harmonogramowaniem:** MRP daje „co i kiedy”; harmonogramowanie
ustala „na której maszynie i w jakiej kolejności”.
"""

version = "0.0.1"
