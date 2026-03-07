"""Knowledge item: backup restore verification."""

title = "Weryfikacja backupu i przywracania"

content = """
Backupy są bezużyteczne, jeśli nie można ich przywrócić. Regularna weryfikacja
procedur backup i restore zapewnia, że w razie awarii dane można odtworzyć.

**Kontekst:** Wielu incydentów związanych z utratą danych można by uniknąć przez
regularne testy restore. Procedury muszą być udokumentowane i ćwiczone.

**Kluczowe działania:**
1) Wykonuj okresowe testy restore (np. kwartalnie) w izolowanym środowisku.
2) Weryfikuj integralność danych po restore.
3) Mierz i dokumentuj RTO (Recovery Time Objective) i RPO (Recovery Point Objective).
4) Aktualizuj procedury po zmianach w architekturze danych.
"""

version = "0.0.1"
