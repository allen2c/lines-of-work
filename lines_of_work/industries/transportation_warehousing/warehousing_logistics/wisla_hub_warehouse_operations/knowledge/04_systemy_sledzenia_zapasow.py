title = "Systemy śledzenia zapasów"

content = """
Wisła Hub wykorzystuje system WMS zintegrowany z ERP w czasie rzeczywistym.
Każda lokalizacja, paleta i jednostka mają unikalny identyfikator skanowalny.

**LPN (License Plate Number):** Każda jednostka logistyczna otrzymuje numer LPN
przy przyjęciu. Numer jest powiązany z SKU, ilością i lokalizacją. Skanowanie
LPN aktualizuje stan w systemie natychmiast.

**Inwentaryzacje cykliczne:** Program ABC określa częstotliwość — produkty A co
tydzień, B co miesiąc, C co kwartał. Rozbieżności powyżej 2% wywołują audyt
i blokadę lokalizacji do wyjaśnienia.

**Bilansowanie:** WMS automatycznie porównuje stan systemowy ze stanem fizycznym
po każdej transakcji krytycznej. Alert przy odchyleniu przekraczającym próg.
"""

version = "0.0.1"
