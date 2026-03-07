"""Knowledge item: komunikasi risiko ke stakeholder."""

title = "Komunikasi Risiko ke Stakeholder"

content = """
Komunikasi risiko yang efektif memastikan pemangku kepentingan memahami status kualitas,
dampak cacat, dan rekomendasi rilis. Tanpa transparansi, keputusan bisnis dibuat tanpa
konteks teknis yang memadai.

**Konteks:** Di lingkungan Agile, stakeholder sering membutuhkan update singkat dan dapat
ditindaklanjuti. Manajer produk membutuhkan ringkasan dampak; tim teknis membutuhkan detail
reproduksi; eksekutif membutuhkan metrik dan tren.

**Langkah Utama:**
1) Siapkan laporan status pengujian berkala dengan metrik kunci (pass rate, cacat terbuka).
2) Kategorikan risiko: blocker, high, medium, low dengan dampak bisnis yang jelas.
3) Sertakan rekomendasi: rilis, tunda, atau rilis dengan mitigasi.
4) Dokumentasikan ketidakpastian dan asumsi saat data tidak lengkap.
5) Gunakan saluran yang sesuai: standup untuk update singkat, dokumen untuk keputusan formal.

**Kriteria Penerimaan:** Stakeholder dapat menjawab "apakah kita siap rilis?" berdasarkan
informasi yang diberikan. Rekomendasi didukung oleh bukti dan metrik.

**Kegagalan Umum:** Terlalu teknis untuk audiens non-teknis, menyembunyikan risiko untuk
menghindari konflik, atau tidak membedakan antara kepastian dan estimasi.
"""

version = "0.0.1"
