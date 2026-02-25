title = "Transaksi Terdistribusi dan Konsistensi"

content = """
Transaksi klasik (ACID) sulit di lingkungan terdistribusi. Integrasi yang melibatkan banyak
sistem harus memilih model konsistensi yang sesuai dengan kebutuhan bisnis dan trade-off.

**Two-Phase Commit (2PC):** Koordinator memastikan semua peserta setuju sebelum commit.
Blocking, rentan terhadap timeout dan deadlock. Cocok untuk sistem yang mendukung XA.
Sering dihindari untuk integrasi skala besar karena kompleksitas dan availability.

**Saga:** Urutan transaksi lokal; setiap langkah memiliki kompensasi jika langkah berikutnya
gagal. Compensating transaction membatalkan efek yang sudah dilakukan. Eventual consistency;
bisnis harus menerima window inkonsistensi. Implementasi: choreography (event-driven) atau
orchestration (central coordinator).

**Pilihan Praktis:** Banyak integrasi menggunakan at-least-once delivery plus idempotensi
di sisi konsumen. Untuk operasi kritis, pertimbangkan outbox pattern untuk memastikan
pesan terkirim transaksional dengan pembaruan bisnis.
"""  # noqa: E501

version = "0.0.1"
