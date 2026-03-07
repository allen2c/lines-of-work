"""Knowledge item: end to end user flows."""

title = "Przepływy użytkownika end-to-end"

content = """
Testy E2E symulują rzeczywiste ścieżki użytkownika od wejścia do wyjścia z systemu.
W Odra Valley priorytetem są krytyczne ścieżki biznesowe: rejestracja, logowanie, kluczowe
transakcje, eksport danych. Testy E2E są kosztowne w utrzymaniu; należy je ograniczyć do
minimum koniecznego dla pewności release.

**Kontekst:** E2E wykrywają problemy, które testy niższego poziomu pomijają (np. błędy
UI, timeouty sieciowe). Są jednak wolne i podatne na flakiness.

**Kluczowe działania:**
1) Zidentyfikuj 5–10 krytycznych user flows na produkt.
2) Automatyzuj za pomocą Selenium, Playwright lub równoważnego narzędzia.
3) Uruchamiaj E2E przed release; rozważ równoległe wykonanie dla skrócenia czasu.
4) Izoluj testy od siebie (np. unikalne dane testowe per run).
"""

version = "0.0.1"
