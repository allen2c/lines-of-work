"""Knowledge item: secrets management checks."""

title = "Kontrole zarządzania sekretami"

content = """
Sekrety (hasła, klucze API, certyfikaty) nie mogą trafiać do kodu źródłowego ani logów.
Kontrole zarządzania sekretami weryfikują, czy polityka jest przestrzegana w całym pipeline.

**Kontekst:** Wyciek sekretu może prowadzić do kompromitacji całego systemu. Narzędzia takie
jak git-secrets, truffleHog lub skanery SAST pomagają wykryć przypadkowe commity.

**Kluczowe działania:**
1) Skanuj repozytoria pod kątem wzorców sekretów (regex, słowniki).
2) Weryfikuj, że zmienne środowiskowe i vault są używane zamiast hardcodowanych wartości.
3) Sprawdź rotację kluczy i politykę wygasania.
4) Upewnij się, że logi i metryki nie zawierają wrażliwych danych.
5) Zdefiniuj procedurę reakcji na wyciek sekretu.
"""

version = "0.0.1"
