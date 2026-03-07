title = "Architektura oparta na zdarzeniach"

content = """
W architekturze event-driven komponenty komunikują się przez zdarzenia publikowane
do brokerów (Kafka, RabbitMQ, AWS EventBridge). Producent nie zna konsumentów;
konsument subskrybuje tematy lub kolejki.

**Zalety:** Luźne powiązanie, skalowalność, odporność na chwilowe niedostępności.
Wiele konsumentów może reagować na to samo zdarzenie. Audyt i replay możliwe
przy logu zdarzeń.

**Wyzwania:** Spójność eventual, brak transakcji rozproszonych, trudniejszy debug.
Sekwencjonowanie i kolejność zdarzeń wymaga uwagi (partycje, klucze).

**Schemat zdarzeń:** Używaj Avro, Protobuf lub JSON Schema z rejestrem. Wersjonuj
pola; nowe pola opcjonalne. Nie usuwaj pól bez deprecation.
"""  # noqa: E501

version = "0.0.1"
