title = "Apache Kafka – Grundlagen"

content = """
Apache Kafka ist eine verteilte Event-Streaming-Plattform. Sie ermöglicht
Echtzeit-Datenflüsse zwischen Systemen mit hohem Durchsatz und Persistenz.

**Topics und Partitionen:** Nachrichten werden in Topics gespeichert. Jedes
Topic ist in Partitionen unterteilt; Nachrichten mit gleichem Key landen in
derselben Partition. Partitionen ermöglichen parallelen Konsum.

**Producer und Consumer:** Producer schreiben in Topics; Consumer lesen in
Consumer Groups. Jede Partition wird von genau einem Consumer pro Group
gelesen. Consumer Lag misst die Verzögerung zwischen neuester Nachricht und
aktuellem Leseoffset.

**Broker und Replikation:** Kafka-Cluster bestehen aus Brokern. Jede Partition
wird repliziert; ein Leader nimmt Schreibvorgänge entgegen, Replicas halten
Kopien. Ausfälle werden durch Leader-Election abgefangen.
"""

version = "0.0.1"
