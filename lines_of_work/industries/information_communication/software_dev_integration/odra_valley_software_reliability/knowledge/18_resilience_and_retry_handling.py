"""Knowledge item: resilience and retry handling."""

title = "Odporność i obsługa ponownych prób"

content = """
Odporność systemu na awarie zewnętrzne (sieć, zależności) wymaga poprawnej implementacji
retry, backoff, circuit breaker i fallback. Testy muszą weryfikować zachowanie przy
timeoutach, błędach 5xx i częściowych awariach. Odra Valley stosuje wzorce z Resilience4j
lub równoważnych bibliotek.

**Kontekst:** Zewnętrzne usługi zawodzą; system musi degradować się łagodnie zamiast
kaskadowych awarii. Retry bez limitów może pogorszyć sytuację (thundering herd).

**Kluczowe działania:**
1) Zdefiniuj polityki retry (max attempts, backoff) dla każdej zewnętrznej zależności.
2) Implementuj circuit breaker przy powtarzających się awariach.
3) Testuj scenariusze: timeout, 5xx, częściowa niedostępność.
4) Monitoruj metryki circuit breaker (stan, liczba odrzuceń).
"""

version = "0.0.1"
