"""Knowledge item: contract testing strategy."""

title = "Strategia testów kontraktowych"

content = """
Testy kontraktowe weryfikują, że konsumenci i dostawcy API są zgodni z ustalonym kontraktem
(schema, format, semantyka). Zapobiegają awariom przy niezależnym wdrażaniu mikrousług.
Odra Valley stosuje Pact lub równoważne narzędzie dla API wewnętrznych.

**Kontekst:** W architekturze mikrousług zmiana kontraktu przez jedną usługę może złamać
innych. Testy kontraktowe wykrywają niezgodności przed wdrożeniem.

**Kluczowe działania:**
1) Zdefiniuj kontrakty (OpenAPI, Pact) dla wszystkich publicznych API.
2) Generuj testy konsumenta i dostawcy z kontraktów.
3) Uruchamiaj testy kontraktowe w CI obu stron.
4) Wersjonuj kontrakty; obsługuj deprecation z wyprzedzeniem.
"""

version = "0.0.1"
