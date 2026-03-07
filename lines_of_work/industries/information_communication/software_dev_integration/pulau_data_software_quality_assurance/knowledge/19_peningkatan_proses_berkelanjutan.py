"""Knowledge item: peningkatan proses berkelanjutan."""

title = "Peningkatan Proses Berkelanjutan"

content = """
Peningkatan proses berkelanjutan berarti belajar dari cacat yang lolos, pola kegagalan
yang berulang, dan umpan balik tim. QA tidak hanya menemukan cacat tetapi juga
mengusulkan perbaikan pada proses pengembangan dan pengujian.

**Konteks:** Tim yang tidak merefleksikan root cause cenderung mengulangi kesalahan.
Retrospektif, analisis post-mortem insiden, dan metrik tren cacat adalah masukan untuk
peningkatan proses.

**Langkah Utama:**
1) Kategorikan cacat berdasarkan tipe, area, dan fase pengenalan (dev, QA, produksi).
2) Identifikasi pola: cacat yang sering muncul di area tertentu atau dari tim tertentu.
3) Usulkan action item: checklist tambahan, review kode, pelatihan, alat baru.
4) Lacak efektivitas: apakah insiden serupa berkurang setelah perubahan proses?
5) Bagikan pembelajaran ke seluruh tim dalam format yang dapat ditindaklanjuti.

**Kriteria Penerimaan:** Setiap insiden produksi atau pola cacat berulang memiliki
action item yang terdokumentasi. Tim meninjau efektivitas perubahan secara berkala.

**Kegagalan Umum:** Menyalahkan individu tanpa memperbaiki proses, mengabaikan metrik
tren, atau tidak menindaklanjuti action item hingga selesai.
"""

version = "0.0.1"
