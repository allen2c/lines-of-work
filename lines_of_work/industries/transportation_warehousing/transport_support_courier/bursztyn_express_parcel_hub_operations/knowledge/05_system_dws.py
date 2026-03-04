title = "DWS — dynamiczne ważenie i skanowanie"

content = """
DWS (Dynamic Weighing and Scanning) mierzy masę i wymiary paczki w ruchu, równolegle
ze skanowaniem. Dane są przekazywane do systemu WMS i służą do routingu, rozliczeń
i wykrywania rozbieżności (np. zadeklarowana vs. rzeczywista masa).

**Parametry mierzone:**
- Masa (kg)
- Długość, szerokość, wysokość (cm)
- Objętość obliczana (L×W×H) — używana do wymiarowej taryfikacji

**Wykorzystanie:**
- Weryfikacja przed sortacją: nadwaga lub nadwymiar → kierunek specjalny
- Dane dla rozliczeń z nadawcą i dla taryf wymiarowych
- Statystyki obciążenia tras i optymalizacji ładunku
"""  # noqa: E501

version = "0.0.1"
