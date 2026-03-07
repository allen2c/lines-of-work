"""Knowledge item: synthetic data generation."""

title = "Generowanie danych syntetycznych"

content = """
Dane syntetyczne są generowane programowo zamiast pochodzić z produkcji lub ręcznych
fixture'ów. Umożliwiają testowanie edge case'ów, skalowanie oraz unikanie problemów
prywatności przy użyciu danych produkcyjnych.

**Kontekst:** Generatory muszą produkować dane realistyczne pod względem formatu,
zakresów i relacji. Niewłaściwa synteza prowadzi do testów, które przechodzą na
sztucznych danych, ale zawodzą na danych rzeczywistych.

**Kluczowe działania:**
1) Wybierz podejście: deterministyczne generatory, Faker-like biblioteki, lub
   modele uczenia maszynowego dla złożonych struktur.
2) Zdefiniuj schematy i ograniczenia (np. unikalność, relacje między encjami).
3) Weryfikuj realizm: porównaj rozkłady z danymi referencyjnymi gdzie to możliwe.
4) Udokumentuj założenia i ograniczenia generatorów.
5) Przeglądaj i aktualizuj generatory przy zmianie modeli domenowych.
"""

version = "0.0.1"
