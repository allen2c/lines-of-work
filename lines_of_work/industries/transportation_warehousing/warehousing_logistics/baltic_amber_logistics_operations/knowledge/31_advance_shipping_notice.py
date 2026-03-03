title = "ASN — Advance Shipping Notice i weryfikacja"

content = """
ASN (Advance Shipping Notice) to wczesna informacja od dostawcy
o nadchodzącej przesyłce. Zawiera listę pozycji, ilości, datę
przybycia. Magazyn używa ASN do planowania odbioru i weryfikacji.

**Zawartość ASN:** Numer referencyjny, data wysyłki, przewoźnik,
 lista pozycji (SKU, ilość, waga), numer SAD lub T1 jeśli dotyczy.
Otrzymywane co najmniej 24 h przed przybyciem.

**Weryfikacja:** Przy odbiorze porównujemy fizyczną zawartość
z ASN. Rozbieżności odnotowane w systemie. Brak ASN — przyjęcie
w trybie manualnym, eskalacja do dostawcy o brak informacji.

**Integracja WMS:** ASN tworzy oczekiwane pozycje w systemie.
Fizyczny odbiór potwierdza lub koryguje stan. Powiązanie
ASN–SAD–fizyczna lokalizacja.
"""  # noqa: E501

version = "0.0.1"
