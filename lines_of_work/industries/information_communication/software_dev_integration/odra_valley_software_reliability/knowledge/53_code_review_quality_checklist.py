"""Knowledge item: code review quality checklist."""

title = "Checklista jakości code review"

content = """
Code review stanowi pierwszą linię obrony przed defektami. Checklista jakości pomaga
recenzentom skupić się na aspektach istotnych dla niezawodności: obsłudze błędów,
transakcjach, retry, idempotentności i logowaniu.

**Kontekst:** Recenzje skupione wyłącznie na stylu kodu pomijają ryzyka związane z
awariami w produkcji. Checklista powinna być dostosowana do architektury i wzorców
używanych w projekcie.

**Kluczowe działania:**
1) Zdefiniuj punkty checklisty specyficzne dla niezawodności (np. retry, timeouts).
2) Wymagaj recenzji dla zmian w krytycznych ścieżkach i integracjach.
3) Udokumentuj typowe problemy i jak ich unikać.
4) Przeglądaj i aktualizuj checklistę po incydentach.
"""

version = "0.0.1"
