title = "Retry i exponential backoff"

content = """
Retry z exponential backoff to standardowa technika radzenia sobie z przejściowymi
błędami w integracjach. Zwiększa szansę na sukces przy tymczasowych awariach sieci
lub przeciążeniu systemu docelowego.

**Exponential backoff:** Opóźnienie między próbami rośnie wykładniczo: 1s, 2s, 4s, 8s...
Formuła: delay = base * 2^attempt. Ogranicz maksymalne opóźnienie (np. 60s) i liczbę
prób (np. 5).

**Jitter:** Dodaj losową zmienność do opóźnienia, aby uniknąć thundering herd — gdy
wielu klientów retry w tym samym momencie. Jitter = delay * (0.5 + random()).

**Kiedy retry:** Tylko przy błędach przejściowych (timeout, 5xx, 429). Nigdy przy
4xx (oprócz 429) — błąd klienta nie zniknie po powtórzeniu.

**Implementacja:** Używaj bibliotek (tenacity, resilience4j) zamiast pisać własną
pętlę. Konfiguruj timeout całkowity, aby retry nie trwały w nieskończoność.
"""  # noqa: E501

version = "0.0.1"
