title = "Opcje integracji AWS"

content = """
AWS oferuje wiele usług wspierających integrację systemów. Lambda pozwala na serwerless
przetwarzanie zdarzeń i wywołań API. API Gateway zarządza REST i WebSocket API.
EventBridge łączy aplikacje za pomocą zdarzeń. SQS i SNS obsługują kolejkowanie
wiadomości i pub/sub. Kinesis przetwarza strumienie danych w czasie rzeczywistym.

**Wybór usługi:** Lambda dla transformacji i orkiestracji, SQS dla niezawodnej kolejki,
EventBridge dla routingu zdarzeń między usługami. Rozważ koszty, opóźnienia i
wymagania dotyczące trwałości przed wyborem architektury.
"""  # noqa: E501

version = "0.0.1"
