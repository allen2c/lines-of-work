"""Knowledge item: environment consistency strategy."""

title = "Strategia spójności środowisk"

content = """
Spójność środowisk (dev, stage, production) jest kluczowa dla wiarygodności testów.
Różnice w konfiguracji, wersjach zależności lub danych prowadzą do sytuacji, w których
testy przechodzą lokalnie, ale produkcja zawodzi.

**Kontekst:** Infrastruktura jako kod (IaC), konteneryzacja i zarządzanie konfiguracją
przez zmienne środowiskowe muszą być zsynchronizowane. Dokumentuj drift i planuj
regularne audyty spójności.

**Kluczowe działania:**
1) Zdefiniuj canonical source dla konfiguracji każdego środowiska.
2) Automatyzuj provision środowisk testowych z tych samych szablonów co production.
3) Wykonuj porównania konfiguracji przed krytycznymi release'ami.
4) Udokumentuj dozwolone różnice (np. limity, feature flags) i ich uzasadnienie.
"""

version = "0.0.1"
