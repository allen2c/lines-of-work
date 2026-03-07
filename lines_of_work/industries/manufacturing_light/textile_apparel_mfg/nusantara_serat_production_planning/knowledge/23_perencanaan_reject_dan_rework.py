"""Rejection and rework planning in production flow."""

title = "Perencanaan Reject dan Rework"

content = """
Reject dan rework mempengaruhi kapasitas efektif dan jadwal. Perencanaan produksi
harus mengalokasikan buffer untuk defect rate historis dan waktu rework.

**Buffer reject:** Berdasarkan data AQL dan defect rate per style, tambahkan 2–5%
ke quantity yang dijadwalkan untuk menutupi reject yang tidak bisa dirework.

**Slot rework:** Alokasikan waktu di akhir shift atau di antara batch untuk unit
yang bisa diperbaiki. Rework tidak boleh memblokir aliran utama.

**Eskalasi:** Jika reject rate melebihi 5%, hentikan produksi dan eskalasi ke QA
dan produksi. Perbaiki root cause sebelum melanjutkan.
"""  # noqa: E501

version = "0.0.1"
