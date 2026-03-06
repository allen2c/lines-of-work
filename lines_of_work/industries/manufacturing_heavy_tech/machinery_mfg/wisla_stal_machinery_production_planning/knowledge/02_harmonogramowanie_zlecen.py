title = "Harmonogramowanie zleceń produkcyjnych"

content = """
Harmonogramowanie to przypisanie zleceń do konkretnych maszyn, zmian i terminów.
W Wisła Stal stosuje się harmonogramowanie skończonej zdolności (finite capacity)
z uwzględnieniem priorytetów klientów i terminów dostaw.

**Reguły priorytetyzacji:** Termin dostawy (EDD), krytyczność klienta, wartość
zlecenia, czas realizacji. Konflikty rozstrzyga kierownik planowania.

**Czasy przezbrojenia:** Każda zmiana rodzaju obrabianego detalu wymaga setupu.
Czasy przezbrojenia są wpisane w system ERP i wpływają na dostępność maszyn.

**Kolejki:** Zlecenia w kolejce do danej maszyny są sortowane według reguły
priorytetowej. Przeładowanie kolejki prowadzi do opóźnień kaskadowych.
"""

version = "0.0.1"
