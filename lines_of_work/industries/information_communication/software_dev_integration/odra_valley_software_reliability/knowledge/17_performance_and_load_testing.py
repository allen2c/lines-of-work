"""Knowledge item: performance and load testing."""

title = "Testy wydajności i obciążenia"

content = """
Testy wydajności i obciążenia mierzą czas odpowiedzi, przepustowość i zachowanie systemu
pod wzrastającym obciążeniem. Odra Valley wymaga testów load przed release dla usług
krytycznych; wyniki muszą mieścić się w zdefiniowanych SLO (np. p99 < 500ms).

**Kontekst:** Awarie wydajności w produkcji wpływają bezpośrednio na doświadczenie
użytkownika i koszty infrastruktury. Wczesne wykrywanie bottlenecków oszczędza czas i
środki.

**Kluczowe działania:**
1) Zdefiniuj scenariusze obciążenia (RPS, wzorce użytkowników) na podstawie metryk
   produkcyjnych.
2) Uruchamiaj testy load w dedykowanym środowisku przed release.
3) Monitoruj metryki: latency, throughput, error rate, wykorzystanie zasobów.
4) Dokumentuj baseline i alertuj przy znaczącej degradacji.
"""

version = "0.0.1"
