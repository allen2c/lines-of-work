title = "Kolejki komunikatów"

content = """
Kolejki komunikatów (RabbitMQ, Apache Kafka, AWS SQS, Azure Service Bus) zapewniają
asynchroniczną, odznaczoną komunikację między systemami. Odciążają nadawcę od
bezpośredniego oczekiwania na odbiorcę.

**Wzorce:** Point-to-point (kolejka) — jeden konsument przetwarza wiadomość.
Publish-subscribe (topic) — wielu subskrybentów otrzymuje kopię. Kafka łączy oba
modele przez consumer groups.

**Gwarancje dostarczenia:** At-most-once, at-least-once, exactly-once. Wybór zależy
od wymagań biznesowych. Exactly-once jest najtrudniejsze do osiągnięcia.

**Idempotentność:** Przy at-least-once wiadomości mogą być dostarczone wielokrotnie.
Konsument musi być idempotentny (np. sprawdzać klucz przed zapisem) lub używać
deduplikacji.

**Monitoring:** Śledź długość kolejki, opóźnienia przetwarzania, dead-letter queues.
Alerty przy nagłym wzroście backlogu.
"""  # noqa: E501

version = "0.0.1"
