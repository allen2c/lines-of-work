"""Knowledge item: error budget implementation."""

title = "Wdrożenie budżetu błędów"

content = """
Budżet błędów (error budget) to dopuszczalna ilość niedostępności lub błędów,
którą zespół może „wydać” w danym okresie. Łączy SLO z decyzjami o release'ach
i priorytetach naprawy.

**Kontekst:** Gdy budżet jest wyczerpany, nowe wdrożenia są wstrzymywane do
odtworzenia budżetu. Gdy budżet jest duży, można akceptować wyższe ryzyko
w zamian za szybszą dostawę wartości.

**Kluczowe działania:**
1) Zdefiniuj SLO dla kluczowych usług (np. 99.9% dostępności).
2) Oblicz budżet jako (1 - SLO) * okres (np. miesięczny).
3) Zintegruj budżet z pipeline'em release: blokuj deploy przy wyczerpaniu.
4) Przeglądaj wykorzystanie budżetu w retrospektywach i dostosuj SLO.
"""

version = "0.0.1"
