title = "Skanery i RFID w integracji z WMS"

content = """
Skanery kodu kreskowego i opcjonalnie RFID umożliwiają
szybki i bezbłędny odczyt identyfikatorów. WMS otrzymuje
dane w czasie rzeczywistym, co eliminuje błędy ręcznego
wpisu.

**Skanowanie przy odbiorze:** Każda jednostka (karton,
paleta) skanowana przed putaway. WMS weryfikuje zgodność
z ASN. Nieznany kod — blokada, eskalacja.

**Skanowanie przy kompletacji:** Lokalizacja → SKU → ilość.
Potwierdzenie skanem. Błąd — alert, ponowna kompletacja.

**Skanowanie przy wysyłce:** Etykieta przewozowa, lista
pakowa. Potwierdzenie zamknięcia zamówienia w WMS.

**RFID:** Stosowane dla palet w strefie rezerwowej lub
dla szybkiego liczenia. Czytniki przy bramach. Koszty
wyższe, korzyść przy dużych wolumenach.
"""  # noqa: E501

version = "0.0.1"
