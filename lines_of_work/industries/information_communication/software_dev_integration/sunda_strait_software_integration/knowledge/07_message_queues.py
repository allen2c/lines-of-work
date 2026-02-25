title = "Message Queues untuk Integrasi Asinkron"

content = """
Message queue mendekopel produsen dan konsumen, memungkinkan integrasi asinkron yang
andal dan dapat diskalakan. Pesan dikirim ke queue; konsumen memproses sesuai kapasitas.

**Model:** Point-to-point (queue): satu konsumen memproses setiap pesan. Publish-subscribe
(topic): banyak konsumen menerima salinan. Pilih berdasarkan kebutuhan — satu pekerja
vs broadcast.

**Sifat Penting:** At-least-once vs exactly-once delivery. Kebanyakan queue menjamin
at-least-once; konsumen harus idempoten. Persistence mencegah kehilangan pesan saat
restart. Dead-letter queue untuk pesan gagal setelah retry maksimum.

**Implementasi Umum:** RabbitMQ, Apache Kafka, AWS SQS/SNS, Redis Streams. Kafka untuk
event streaming dan replay; SQS untuk job queue sederhana. Pertimbangkan biaya operasional
dan keterampilan tim saat memilih.
"""  # noqa: E501

version = "0.0.1"
