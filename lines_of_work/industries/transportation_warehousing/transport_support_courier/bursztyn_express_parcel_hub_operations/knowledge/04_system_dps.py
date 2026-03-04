title = "System automatycznej sortacji DPS"

content = """
DPS (Destination Processing System) kieruje paczki do korytarzy sortacyjnych na podstawie
odczytu kodu kreskowego. System Bursztyn Express obsługuje kilkaset korytarzy docelowych
i rozpoznaje zarówno formaty krajowe, jak i międzynarodowe (np. S10, S2).

**Przepływ przez DPS:**
- Taśma doprowadza paczkę do czytnika; odczyt 1D/2D jest mapowany na docelowy korytarz.
- W przypadku braku odczytu paczka trafia do linii ręcznej (reject lane).
- Na końcu korytarza pracownik układa paczki w kontenery lub na palety według trasy.

**Utrzymanie:**
Czytniki są kalibrowane codziennie. Wskaźnik odrzutów (reject rate) > 2% wymaga interwencji
— sprawdzenie jakości etykiet u nadawców, ewentualna zmiana taśmy lub czytnika.
"""  # noqa: E501

version = "0.0.1"
