"""Knowledge item: observability alert tuning."""

title = "Dostrajanie alertów obserwowalności"

content = """
Dostrajanie alertów obserwowalności zmniejsza szum i poprawia czas reakcji na rzeczywiste incydenty.
Zespół niezawodności współpracuje z SRE przy definiowaniu progów, agregacji i eskalacji.

**Kontekst:** Zbyt wiele alertów prowadzi do zmęczenia i ignorowania. Zbyt mało opóźnia wykrycie.
Cel: alerty o wysokiej precyzji, niskim false positive rate i jasnej akcji naprawczej.

**Kluczowe działania:**
1) Przeglądaj alerty po każdym incydencie — czy były użyteczne?
2) Agreguj powiązane sygnały, aby uniknąć burzy alertów.
3) Definiuj jasne progi i okna czasowe dla każdego alertu.
4) Testuj ścieżki eskalacji w środowisku staging.
"""

version = "0.0.1"
