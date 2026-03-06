title = "System ERP i moduł MRP"

content = """
Wisła Stal wykorzystuje system ERP z modułem planowania zasobów (MRP/MRP II).
Planista musi znać logikę systemu: jak generowane są zlecenia, jak działa
eksplozja BOM, jak aktualizować zdolność i harmonogram.

**Eksplozja BOM:** System rozbija zlecenie wyrobu gotowego na zapotrzebowanie
na półfabrykaty i materiały według struktury drzewa. Błędy w BOM prowadzą do
błędnych zapotrzebowań.

**Netting:** System porównuje zapotrzebowanie z dostępnym zapasem i generuje
zlecenia na brakującą ilość. Planista weryfikuje wygenerowane zlecenia przed
zatwierdzeniem.

**Integracja z harmonogramem:** Zmiany w harmonogramie wpływają na zapotrzebowanie
materiałowe. Odświeżenie MRP po zmianach harmonogramu jest standardową procedurą.
"""

version = "0.0.1"
