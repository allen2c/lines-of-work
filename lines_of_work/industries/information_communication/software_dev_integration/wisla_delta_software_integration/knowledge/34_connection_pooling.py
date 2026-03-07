title = "Pulowanie połączeń"

content = """
Tworzenie nowego połączenia sieciowego jest kosztowne. Pula połączeń utrzymuje
gotowe połączenia do ponownego użycia, redukując opóźnienia i obciążenie.

**Zasady:** Ustaw rozmiar puli na podstawie równoległości i limitów zdalnego serwera.
Zbyt mała pula — kolejkowanie; zbyt duża — marnowanie zasobów.

**Timeouts:** Połączenia w puli mogą się zestarzeć. Ustaw max lifetime i idle timeout.
Zamknij nieużywane połączenia, aby zwolnić zasoby po stronie serwera.
"""  # noqa: E501

version = "0.0.1"
