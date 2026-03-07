"""Labor planning for production capacity."""

title = "Perencanaan Tenaga Kerja"

content = """
Tenaga kerja adalah sumber daya utama di lini jahit. Perencanaan mencakup jumlah
operator per shift, keterampilan yang dibutuhkan, dan jadwal pelatihan untuk gaya
baru. Kekurangan operator pada operasi kritis memperlambat seluruh lini.

**Rasio operator-mesin:** Bergantung pada kompleksitas operasi, satu operator dapat
mengoperasikan satu atau beberapa mesin. Operasi manual (finishing, packing) membutuhkan
rasio 1:1. Perencanaan memperhitungkan absensi dan turnover historis.

**Pelatihan gaya baru:** Operator membutuhkan waktu untuk mencapai standar output pada
gaya baru. Jadwalkan buffer pelatihan sebelum target produksi bulk dimulai.
"""  # noqa: E501

version = "0.0.1"
