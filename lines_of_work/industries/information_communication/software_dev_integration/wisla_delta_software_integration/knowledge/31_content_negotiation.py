title = "Negocjacja treści (Content Negotiation)"

content = """
Negocjacja treści pozwala klientowi i serwerowi uzgodnić format odpowiedzi (JSON, XML,
protobuf) oraz język. Nagłówki Accept, Accept-Language i Content-Type sterują wyborem.

**Accept:** Klient deklaruje preferowane typy MIME. Serwer zwraca 406 Not Acceptable,
gdy żaden format nie jest obsługiwany. Dla integracji preferuj JSON jako domyślny.

**Content-Type:** Określa format wysyłanego body. Wymagany przy POST/PUT/PATCH.
Brak lub błędny Content-Type prowadzi do odrzucenia żądania.

**Accept-Language:** Dla treści lokalizowanych. W integracjach systemowych często
pomijany — dane są zwykle w jednym języku lub neutralne.
"""  # noqa: E501

version = "0.0.1"
