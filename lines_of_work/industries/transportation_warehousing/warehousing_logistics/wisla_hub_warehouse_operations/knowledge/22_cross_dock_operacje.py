title = "Operacje cross-dock"

content = """
Cross-dock w Wisła Hub obejmuje towary omijające magazynowanie — z rozładunku
bezpośrednio na załadunek. Zastosowanie: transfery między oddziałami, dostawy
just-in-time, produkty z krótką datą ważności.

**Kwalifikacja:** Klient lub WMS oznacza przesyłkę jako cross-dock. Wymagane:
potwierdzony odbiorca, okno czasowe, zgodność dokumentów. Brak którejkolwiek
— przekierowanie do normalnego przyjęcia.

**Przepływ:** Rozładunek do strefy cross-dock (nie do lokacji magazynowych).
Sortowanie według przewoźnika/docelowego oddziału. Konsolidacja jeśli
wymagana. Załadunek na oczekujące pojazdy. Czas w obiekcie: max 4 godziny.

**Raportowanie:** Każda jednostka skanowana przy wejściu i wyjściu. Czas
przebywania rejestrowany. Przekroczenie 4 h — opłata postojowa i powiadomienie klienta.
"""

version = "0.0.1"
