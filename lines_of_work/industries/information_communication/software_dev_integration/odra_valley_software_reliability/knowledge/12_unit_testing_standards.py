"""Knowledge item: unit testing standards."""

title = "Standardy testów jednostkowych"

content = """
Standardy testów jednostkowych w Odra Valley obejmują nazewnictwo, strukturę (Arrange-Act-
Assert), izolację (brak zewnętrznych zależności) oraz pokrycie krytycznych ścieżek. Testy
muszą być deterministyczne i szybkie; flaky testy są traktowane jako defekty wysokiego
priorytetu.

**Kontekst:** Testy jednostkowe stanowią pierwszą linię obrony przed regresją. Słabe
standardy prowadzą do fałszywego poczucia bezpieczeństwa lub nadmiernego utrzymania.

**Kluczowe działania:**
1) Używaj konwencji nazewnictwa: test_<scenariusz>_<oczekiwany_wynik>.
2) Jedna asercja logiczna na test; unikaj testów wielozadaniowych.
3) Mockuj zewnętrzne serwisy i bazy danych.
4) Przeglądaj i aktualizuj standardy w ramach code review.
"""

version = "0.0.1"
