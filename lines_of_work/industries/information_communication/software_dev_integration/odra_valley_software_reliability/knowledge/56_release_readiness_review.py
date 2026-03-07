"""Knowledge item: release readiness review."""

title = "Przegląd gotowości do wydania"

content = """
Release Readiness Review (RRR) to formalna decyzja o tym, czy system spełnia kryteria
do wdrożenia. Uczestniczą w nim przedstawiciele rozwoju, QA, SRE i produktu.

**Kontekst:** RRR zapobiega przedwczesnym wdrożeniom i zapewnia, że wszystkie
interesariusze mają wspólne zrozumienie ryzyka. Brak RRR lub jego formalności
prowadzi do wdrożeń „na żywioł".

**Kluczowe działania:**
1) Zdefiniuj checklistę RRR (testy, metryki, dokumentacja, znane ryzyka).
2) Przeprowadzaj RRR przed każdym release do production.
3) Udokumentuj decyzję (go/no-go) i uzasadnienie.
4) W przypadku no-go ustal plan naprawy i termin kolejnego RRR.
"""

version = "0.0.1"
