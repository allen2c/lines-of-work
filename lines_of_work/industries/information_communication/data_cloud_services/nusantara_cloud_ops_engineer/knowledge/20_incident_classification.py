title = "Klasifikasi dan Prioritas Insiden"

content = """
- Klasifikasi berdasarkan dampak:
  - Kritis: Layanan utama tidak tersedia, pelanggan besar terdampak, atau potensi kehilangan data.
  - Tinggi: Gangguan parsial, performa menurun signifikan, atau satu pelanggan kecil terdampak.
  - Sedang: Gangguan minor, tidak berdampak langsung ke pelanggan (misal: alert suhu, disk hampir penuh).
  - Rendah: Pertanyaan, permintaan informasi, atau perubahan non-produksi.
- Prioritas ditentukan oleh kombinasi dampak dan urgensi:
  - Dampak Kritis + Urgensi Tinggi = Prioritas 1 (P1)
  - Dampak Tinggi + Urgensi Tinggi = P2
  - Dampak Sedang + Urgensi Sedang = P3
  - Dampak Rendah = P4
- P1 harus ditangani segera, P2 dalam 15 menit, P3 dalam 30 menit, P4 dalam 1 jam.
"""  # noqa: E501

version = "0.0.1"
