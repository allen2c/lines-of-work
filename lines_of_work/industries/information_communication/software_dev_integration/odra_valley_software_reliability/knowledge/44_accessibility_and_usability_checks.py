"""Knowledge item: accessibility and usability checks."""

title = "Kontrole dostępności i użyteczności"

content = """
Dostępność (a11y) i użyteczność wpływają na jakość doświadczenia użytkownika oraz
zgodność z regulacjami (np. WCAG, dyrektywy UE). Błędy w tych obszarach mogą
ograniczać dostęp do usługi dla części użytkowników.

**Kontekst:** Testy a11y obejmują nawigację klawiaturą, czytniki ekranu, kontrast
kolorów i semantykę HTML. Użyteczność dotyczy intuicyjności przepływów i obsługi
błędów.

**Kluczowe działania:**
1) Włącz automatyczne skanery a11y (np. axe, Lighthouse) w pipeline CI.
2) Przeprowadzaj ręczne testy z czytnikami ekranu dla krytycznych ścieżek.
3) Zdefiniuj kryteria akceptacji dla użyteczności w PRD.
4) Udokumentuj znane ograniczenia i plany naprawy.
"""

version = "0.0.1"
