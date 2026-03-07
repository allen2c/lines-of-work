"""Knowledge item: observability and logs."""

title = "Obserwowalność i logowanie"

content = """
Obserwowalność umożliwia zrozumienie zachowania systemu w produkcji. Logi, metryki i
tracing stanowią trzy filary: co się wydarzyło, jakie są trendy, gdzie przepływa żądanie.

**Kontekst:** Bez odpowiedniego logowania debugowanie incydentów jest niemożliwe. Logi
muszą być strukturalne (JSON), z odpowiednim poziomem szczegółowości i bez sekretów.

**Kluczowe działania:**
1) Zdefiniuj standard formatu logów (np. timestamp, level, trace_id, message, context).
2) Ustal poziomy: ERROR dla błędów, WARN dla ryzyk, INFO dla kluczowych zdarzeń.
3) Włącz distributed tracing (trace_id, span_id) dla żądań między usługami.
4) Weryfikuj, że logi nie zawierają PII ani sekretów.
5) Określ politykę retencji i archiwizacji logów.
"""

version = "0.0.1"
