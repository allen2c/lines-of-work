"""Perencanaan kapasitas produksi berdasarkan mesin dan tenaga kerja."""

title = "Perencanaan Kapasitas"

content = """
Kapasitas produksi dihitung dari jumlah mesin jahit, jam kerja, dan standar menit
nilai (SMV) per gaya. Nusantara Serat mengoperasikan tiga shift: pagi, siang, malam.

**Rumus Dasar:** Kapasitas harian = (Jumlah mesin × Jam kerja × 60) / SMV rata-rata.
SMV diperoleh dari studi waktu atau data historis per operasi.

**Buffer:** Sediakan buffer 5–10% untuk breakdown mesin, absensi, dan rework.
Kapasitas efektif tidak pernah dijadwalkan 100%.

**Bottleneck:** Identifikasi operasi bottleneck (biasanya jahit atau finishing) dan
jadwalkan sesuai. Overloading bottleneck menyebabkan keterlambatan seluruh lini.
"""  # noqa: E501

version = "0.0.1"
