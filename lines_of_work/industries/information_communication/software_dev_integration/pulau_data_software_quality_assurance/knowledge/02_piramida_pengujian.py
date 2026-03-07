"""Knowledge item: piramida pengujian."""

title = "Piramida Pengujian"

content = """
Piramida pengujian menggambarkan distribusi ideal pengujian: banyak pengujian unit di dasar,
sedikit pengujian integrasi di tengah, dan sedikit pengujian end-to-end di puncak.

**Konteks:** Pengujian unit cepat dan murah; pengujian E2E lambat dan mahal. Keseimbangan
yang tepat memungkinkan umpan balik cepat tanpa mengorbankan kepercayaan terhadap sistem
secara keseluruhan. Untuk tim Agile di Indonesia, piramida membantu mengalokasikan waktu
pengujian secara efisien.

**Struktur:**
- **Dasar (Unit):** 70–80% pengujian. Menguji unit terkecil (fungsi, kelas) secara terisolasi.
- **Tengah (Integrasi):** 15–20% pengujian. Menguji interaksi antar komponen.
- **Puncak (E2E):** 5–10% pengujian. Menguji alur pengguna kritis dari awal hingga akhir.

**Penerapan:** Mulai dengan pengujian unit untuk logika bisnis inti. Tambahkan pengujian
integrasi untuk API dan basis data. Batasi pengujian E2E pada skenario bisnis paling kritis.

**Kegagalan Umum:** Piramida terbalik (banyak E2E, sedikit unit) menyebabkan build lambat
dan perawatan mahal. Atau mengabaikan pengujian integrasi sehingga cacat terdeteksi terlambat.
"""

version = "0.0.1"
