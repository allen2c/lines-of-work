title = "Metody rotacji zapasów: FIFO, FEFO, LIFO"

content = """
Wisła Hub stosuje różne metody rotacji w zależności od rodzaju produktu.
Wybór metody jest ustawiany w WMS na poziomie kategorii SKU.

**FIFO (First In, First Out):** Towary przyjęte wcześniej są wydawane wcześniej.
Stosowane dla większości produktów ogólnych. Zapobiega starzeniu się zapasów.
WMS kieruje kompletację do lokalizacji z najstarszą datą przyjęcia.

**FEFO (First Expiry, First Out):** Priorytet ma data ważności. Obowiązkowe
dla produktów spożywczych, farmaceutycznych i chemicznych. System blokuje
wydanie produktów po dacie ważności.

**LIFO (Last In, First Out):** Stosowane wyjątkowo, np. dla materiałów budowlanych
składowanych na zewnątrz, gdzie warstwa wierzchnia jest najłatwiej dostępna.
Wymaga zatwierdzenia Kierownika Magazynu.
"""

version = "0.0.1"
