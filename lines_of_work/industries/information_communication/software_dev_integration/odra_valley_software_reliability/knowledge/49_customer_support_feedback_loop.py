"""Knowledge item: customer support feedback loop."""

title = "Pętla informacji zwrotnej od wsparcia klienta"

content = """
Informacje od działu wsparcia klienta są cennym źródłem danych o rzeczywistych
problemach w produkcji. Zespół niezawodności powinien systematycznie analizować
te dane i włączać je do planów testów i priorytetyzacji defektów.

**Kontekst:** Wsparcie widzi wzorce: powtarzające się błędy, niejasne komunikaty,
problemy z konkretnymi konfiguracjami. Te dane często nie trafiają do bugtrackera
w ustrukturyzowanej formie.

**Kluczowe działania:**
1) Ustal kanał regularnego przekazywania zgłoszeń od wsparcia do zespołu QA.
2) Kategoryzuj zgłoszenia według obszaru (np. integracja, UI, wydajność).
3) Włącz typowe scenariusze z zgłoszeń do regression suite.
4) Zamknij pętlę: informuj wsparcie o naprawach i workaroundach.
"""

version = "0.0.1"
