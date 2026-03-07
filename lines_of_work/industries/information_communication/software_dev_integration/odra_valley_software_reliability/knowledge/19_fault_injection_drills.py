"""Knowledge item: fault injection drills."""

title = "Ćwiczenia z wstrzykiwaniem błędów"

content = """
Wstrzykiwanie błędów (fault injection) symuluje awarie w kontrolowany sposób: opóźnienia
sieci, błędy dysku, zabicie procesów. Ćwiczenia te ujawniają słabe punkty systemu i
weryfikują procedury odzyskiwania. Odra Valley przeprowadza je regularnie w środowisku
stage lub w wybranych częściach produkcji (chaos engineering).

**Kontekst:** Systemy często nie są testowane pod kątem awarii; pierwsza prawdziwa awaria
ujawnia nieprzygotowanie. Kontrolowane ćwiczenia redukują ryzyko.

**Kluczowe działania:**
1) Zdefiniuj scenariusze: opóźnienie sieci, niedostępność bazy, zabicie węzła.
2) Uruchamiaj w środowisku stage przed produkcją.
3) W produkcji stosuj chaos engineering ostrożnie, z możliwością szybkiego wycofania.
4) Dokumentuj wnioski i poprawki po każdym ćwiczeniu.
"""

version = "0.0.1"
