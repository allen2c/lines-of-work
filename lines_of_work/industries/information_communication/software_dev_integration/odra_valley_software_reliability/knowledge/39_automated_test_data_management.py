"""Knowledge item: automated test data management."""

title = "Automatyczne zarządzanie danymi testowymi"

content = """
Dane testowe muszą być spójne, izolowane i powtarzalne, aby testy dawały wiarygodne
wyniki. Ręczne zarządzanie danymi jest podatne na błędy i nie skaluje się przy
rosnącej liczbie testów i środowisk.

**Kontekst:** Dane testowe obejmują fixture'y, seed data, mockowane odpowiedzi
zewnętrznych API oraz dane syntetyczne. Muszą spełniać wymagania prywatności
i nie zanieczyszczać środowisk współdzielonych.

**Kluczowe działania:**
1) Zdefiniuj źródła danych testowych: fixture'y w repo, bazy seed, generatory.
2) Zapewnij izolację: każdy test lub klasa testów ma własny zestaw danych.
3) Automatyzuj reset/seed przed zestawem testów w CI.
4) Udokumentuj zależności między danymi a scenariuszami testowymi.
5) Przeglądaj zgodność z polityką prywatności (np. brak danych osobowych).
"""

version = "0.0.1"
