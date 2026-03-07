"""Knowledge item: regression suite maintenance."""

title = "Utrzymanie zestawu testów regresyjnych"

content = """
Zestaw testów regresyjnych musi być utrzymywany w dobrej kondycji, aby zachować wartość
i szybkość wykonywania. Zaniedbany zestaw staje się wolny, niestabilny i ignorowany,
co prowadzi do utraty ochrony przed regresją.

**Kontekst:** Testy regresyjne pokrywają krytyczne ścieżki i scenariusze, które nie mogą
ulec degradacji. Wymagają regularnego przeglądu, aktualizacji przy zmianie API lub
logiki oraz usuwania testów zbędnych lub flaky.

**Kluczowe działania:**
1) Przeglądaj zestaw co sprint: identyfikuj testy flaky, duplikaty i martwe testy.
2) Priorytetyzuj testy według krytyczności pokrywanego scenariusza.
3) Ustal SLA na czas wykonania zestawu; dziel na warstwy (szybka/specjalna) jeśli
   przekracza próg.
4) Udokumentuj właściciela każdego testu lub modułu.
5) Zintegruj wyniki z systemem raportowania i alertów.
"""

version = "0.0.1"
