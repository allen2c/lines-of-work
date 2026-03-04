title = "Załadunek pojazdów liniowych i skanowanie out-gate"

content = """
Załadunek na pojazdy liniowe odbywa się według harmonogramu tras. Paczki posegregowane
według celu docelowego są układane w kontenerach lub na paletach i ładowane do naczepy.
Skan out-gate potwierdza fizyczne opuszczenie huba i aktualizuje status śledzenia.

**Procedura załadunku:**
1. Kierowca melduje pojazd; system przypisuje listę paczek do trasy.
2. Pracownicy ładują paczki według kolejności (ostatnia na trasie — pierwsza do rozładunku).
3. Skanowanie out-gate zbiorcze lub per sztuka — zależnie od systemu.
4. Generowanie manifestu trasy i przekazanie kierowcy.

**Rozbieżności:**
Przesyłka w systemie, brak fizycznie w naczepie → blokada, ponowna weryfikacja. Przesyłka
fizycznie załadowana bez skanu → uzupełnienie skanu przed odjazdem.
"""  # noqa: E501

version = "0.0.1"
