title = "Planowanie fal kompletacji"

content = """
Fale kompletacyjne w Wisła Hub grupują zamówienia do realizacji w określonym
oknie czasowym. Planowanie fal pozwala zrównoważyć obciążenie i spełnić terminy
dostaw przewoźników.

**Kryteria grupowania:** Zamówienia grupowane według przewoźnika, okna załadunku,
priorytetu (express przed standard) oraz strefy docelowej. Fala nie może
przekraczać zdolności strefy pakowania.

**Harmonogram:** Fale uruchamiane są co 2-4 godziny w zależności od wolumenu.
Kompletacja musi zakończyć się minimum 90 minut przed wyjazdem przewoźnika.
Opóźnienia wymagają natychmiastowej eskaluacji.

**Metryki:** Średni czas realizacji fali, odsetek zamówień w terminie, wykorzystanie
stref pakowania. Cel: 95% fal zakończonych przed deadlinem.
"""

version = "0.0.1"
