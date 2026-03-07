title = "Wzorzec Circuit Breaker"

content = """
Circuit breaker chroni system przed kaskadowymi awariami, gdy zdalna usługa nie odpowiada.
Przechodzi przez stany: zamknięty (normalny ruch), otwarty (odrzucanie żądań), półotwarty (test).

**Zamknięty:** Żądania przechodzą. Po przekroczeniu progu błędów przechodzi do otwartego.

**Otwarty:** Wszystkie żądania są odrzucane bez wywołania zdalnej usługi. Po timeout przechodzi do półotwartego.

**Półotwarty:** Ograniczona liczba żądań testowych. Sukces → zamknięty; porażka → otwarty.
"""  # noqa: E501

version = "0.0.1"
