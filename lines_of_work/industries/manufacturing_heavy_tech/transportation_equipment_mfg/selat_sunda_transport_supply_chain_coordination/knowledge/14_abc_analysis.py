"""Analisis ABC untuk prioritisasi inventori dan pengadaan."""

title = "Analisis ABC"

content = """
Analisis ABC mengelompokkan item berdasarkan nilai penggunaan tahunan (annual usage ×
unit cost). Kelas A: 20% item yang menyumbang ~80% nilai — prioritas tinggi untuk
pengawasan dan optimasi. Kelas B: item menengah. Kelas C: banyak item nilai rendah —
pengelolaan sederhana.

**Penerapan**: Item A dapat Just-in-Time dengan pemasok terpercaya; item C dapat
stok tinggi dengan review jarang. Safety stock dan cycle count frequency juga dapat
disesuaikan per kelas.

**Pelengkap**: Pertimbangkan criticality (single-source, long lead time) sebagai
dimensi lain. Item low-value tetapi critical tetap butuh perhatian.
"""  # noqa: E501

version = "0.0.1"
