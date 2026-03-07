"""Knowledge item: domain model validation."""

title = "Walidacja modelu domenowego"

content = """
Model domenowy odzwierciedla reguły biznesowe i stany systemu. Błędy w modelu prowadzą do
niespójności danych, błędnych transakcji oraz trudnych do zdiagnozowania awarii w produkcji.

**Kontekst:** Walidacja modelu domenowego obejmuje testy jednostkowe reguł biznesowych,
testy integracyjne przepływu stanów oraz weryfikację spójności z wymaganiami z PRD.

**Kluczowe działania:**
1) Zidentyfikuj reguły biznesowe krytyczne dla niezawodności.
2) Napisz testy jednostkowe dla każdej reguły z granicznymi przypadkami.
3) Zweryfikuj, że model obsługuje stany nieoczekiwane (np. duplikaty, race conditions).
4) Udokumentuj założenia modelu i ich wpływ na testy.
5) Przeglądaj model przy zmianach wymagań domenowych.
"""

version = "0.0.1"
