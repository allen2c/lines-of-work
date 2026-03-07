title = "Audytowanie integracji"

content = """
Integracje przetwarzające dane wrażliwe lub krytyczne biznesowo wymagają logowania
audytowego. Logi audytu muszą być niezmienne, chronione przed modyfikacją i
przechowywane zgodnie z wymogami regulacyjnymi.

**Co logować:** Identyfikator użytkownika/systemu, akcja (odczyt/zapis), identyfikator
zasobu, timestamp, wynik (sukces/błąd), adres IP lub identyfikator wywołującego.
Unikać logowania pełnej treści danych wrażliwych — tylko metadane lub hashe.

**Retencja:** Zgodnie z RODO i polityką firmy. W Polsce — wymagania ustawowe dla
dokumentacji księgowej i danych osobowych. Logi audytu w Delta Wisły — minimum 7 lat
dla integracji finansowych.
"""

version = "0.0.1"
