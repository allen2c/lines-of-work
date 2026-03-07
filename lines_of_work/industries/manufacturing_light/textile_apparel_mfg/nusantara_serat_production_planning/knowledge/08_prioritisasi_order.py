"""Kriteria dan prosedur prioritisasi order produksi."""

title = "Prioritisasi Order"

content = """
Tidak semua order dapat diproduksi bersamaan. Prioritisasi menentukan urutan
pengerjaan berdasarkan aturan bisnis dan kapasitas terbatas.

**Kriteria:** Tanggal pengiriman (EDD), nilai order, pelanggan strategis, dan
kompleksitas. Order export dengan jadwal kapal biasanya prioritas tinggi.

**Aturan Nusantara Serat:** FEFO (First Expiry, First Out) untuk tanggal
pengiriman; pelanggan A mendapat prioritas atas B; rush order dengan surcharge.

**Konflik:** Jika kapasitas tidak mencukupi, eskalasi ke manajer produksi.
Komunikasi ke pelanggan tentang keterlambatan potensial harus proaktif.
"""  # noqa: E501

version = "0.0.1"
