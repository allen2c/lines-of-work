"""Knowledge item: release quality gates."""

title = "Bramy jakości wydania"

content = """
Bramy jakości (quality gates) definiują warunki, które muszą być spełnione przed przejściem
zmian do kolejnego etapu potoku (PR, stage, production). Zapewniają spójność kryteriów
i uniemożliwiają obejście procesu weryfikacji.

**Kontekst:** Bez jasnych bram jakości zespoły mogą wdrażać zmiany z nieprzetestowanymi
scenariuszami lub ignorować defekty o średnim ryzyku. Bramy muszą być automatyczne tam,
gdzie to możliwe, oraz weryfikowalne przez audyt.

**Kluczowe działania:**
1) Zdefiniuj bramy dla każdego etapu: PR (testy jednostkowe, lint), stage (E2E, integracja),
   production (monitoring, canary).
2) Ustal kryteria przejścia: procent testów zielonych, brak krytycznych defektów, metryki SLO.
3) Zaimplementuj automatyczne blokowanie przy niespełnieniu kryteriów.
4) Udokumentuj proces obejścia w sytuacjach awaryjnych oraz wymagane zatwierdzenia.
5) Przeglądaj i aktualizuj bramy co kwartał w oparciu o dane z incydentów.
"""

version = "0.0.1"
