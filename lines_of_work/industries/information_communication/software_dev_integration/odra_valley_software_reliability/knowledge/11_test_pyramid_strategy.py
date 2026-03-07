"""Knowledge item: test pyramid strategy."""

title = "Strategia piramidy testów"

content = """
Piramida testów określa proporcje między testami jednostkowymi, integracyjnymi i end-to-end.
Większość testów powinna być szybka i izolowana (jednostkowe), mniej integracyjnych, najmniej
E2E. Zespół Odra Valley stosuje tę strukturę, aby zachować krótki czas feedbacku przy
wystarczającym pokryciu krytycznych ścieżek.

**Kontekst:** Testy jednostkowe są tanie i szybkie; E2E są wolne i kruche. Równowaga między
szybkością a pewnością decyduje o efektywności CI/CD i zdolności do częstych wdrożeń.

**Kluczowe działania:**
1) Zdefiniuj docelowe proporcje (np. 70% jednostkowe, 20% integracyjne, 10% E2E).
2) Przeglądaj piramidę przy każdym większym refaktoringu.
3) Unikaj testów integracyjnych tam, gdzie wystarczy jednostkowy z mockami.
4) Rezerwuj E2E dla krytycznych user flows i scenariuszy regresji.
"""

version = "0.0.1"
