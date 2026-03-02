title = "Śledzenie przesyłek i komunikacja statusu"

content = """
Po przekazaniu przewoźnikowi magazyn rejestruje numer
śledzenia (tracking) w WMS. Numer przekazywany jest do
działu sprzedaży/obsługi klienta do komunikacji z odbiorcą.

**Proces:** Manifestacja generuje numer tracking. System
przewoźnika zwraca numer w odpowiedzi API lub na etykiecie.
Wpis do WMS → powiadomienie ERP → e-mail/SMS do klienta
(w zależności od konfiguracji).

**Proaktywne śledzenie:** W razie opóźnień zgłoszonych przez
klienta — magazyn może sprawdzić datę przekazania. Problem
po stronie przewoźnika — eskalacja do zespołu transportu.

**Archiwum:** Numery tracking przechowywane z zamówieniem
minimum 2 lata. Ułatwia reklamacje i analizy.
"""  # noqa: E501

version = "0.0.1"
