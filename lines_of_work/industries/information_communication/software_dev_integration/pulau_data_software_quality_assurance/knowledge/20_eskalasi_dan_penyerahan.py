"""Knowledge item: eskalasi dan penyerahan."""

title = "Eskalasi dan Penyerahan"

content = """
Eskalasi dan penyerahan yang tepat memastikan bahwa masalah di luar lingkup QA
ditangani oleh pihak yang berwenang. QA tidak boleh menahan informasi kritis atau
mencoba menyelesaikan masalah yang memerlukan keputusan arsitektur atau bisnis.

**Konteks:** Beberapa temuan memerlukan keputusan CTO (perubahan arsitektur), tim
keamanan (kerentanan), atau manajemen produk (trade-off fitur vs. kualitas). Eskalasi
yang terlambat atau tidak jelas dapat menunda rilis atau memperburuk risiko.

**Langkah Utama:**
1) Definisikan kriteria eskalasi: severity, dampak bisnis, kebutuhan keputusan eksternal.
2) Dokumentasikan temuan dengan bukti, dampak, dan rekomendasi sebelum eskalasi.
3) Tentukan pemilik: siapa yang berwenang mengambil keputusan untuk tiap jenis masalah.
4) Lacak status eskalasi hingga keputusan dibuat dan ditindaklanjuti.
5) Komunikasikan keputusan kembali ke tim dan dokumentasikan untuk referensi.

**Kriteria Penerimaan:** Tidak ada temuan kritis yang tertunda tanpa pemilik yang jelas.
Eskalasi memiliki SLA respons yang disepakati. Keputusan terdokumentasi dan dapat
ditelusuri.

**Kegagalan Umum:** Menunda eskalasi karena takut konflik, mengeskalasi tanpa konteks
yang memadai, atau tidak menindaklanjuti keputusan yang telah dibuat.
"""

version = "0.0.1"
