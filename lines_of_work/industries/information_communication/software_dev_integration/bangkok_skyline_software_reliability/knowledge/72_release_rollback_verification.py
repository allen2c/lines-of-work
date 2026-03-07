"""
Knowledge item 72: release rollback verification. Ensures rollback procedures are
testable, documented, and validated before production deployment.
"""

title = "release rollback verification"

content = """
Verifikasi rollback rilis memastikan bahwa prosedur pengembalian ke versi sebelumnya
dapat dijalankan dengan andal ketika rilis baru menimbulkan insiden atau regresi.
Tanpa verifikasi ini, tim operasi dan SRE tidak memiliki jaminan bahwa rollback akan
berhasil dalam kondisi produksi yang sebenarnya.

**Konteks:** Dalam sistem terdistribusi dengan API, basis data, dan dependensi eksternal,
rollback bukan sekadar membatalkan deploy. Perubahan skema, migrasi data, dan kontrak
API dapat membuat rollback menjadi tidak trivial. Verifikasi harus mencakup skenario
rollback penuh dan sebagian (partial rollback) serta dampaknya terhadap konsumen.

**Prosedur utama:**
1) Dokumentasikan langkah rollback untuk setiap komponen yang di-deploy: urutan
   pengembalian, dependensi antar layanan, dan titik pengambilan keputusan.
2) Uji prosedur rollback di lingkungan staging yang menyerupai produksi, termasuk
   simulasi kegagalan parsial dan waktu pemulihan yang diharapkan.
3) Pastikan skema basis data dan migrasi mendukung rollback mundur (backward
   compatible) atau sediakan skrip rollback migrasi yang telah divalidasi.
4) Verifikasi bahwa feature flag dan konfigurasi dapat dinonaktifkan tanpa
   memerlukan redeploy penuh bila memungkinkan.
5) Tetapkan metrik time-to-rollback (TTR) sebagai target operasional dan ukur
   dalam drill rollback berkala.

**Kriteria penerimaan:** Prosedur rollback dianggap terverifikasi jika telah
dijalankan setidaknya sekali di staging dengan hasil yang terdokumentasi, skrip
atau runbook tersedia dan dapat diakses tim on-call, serta TTR memenuhi SLA
yang ditetapkan.

**Kegagalan umum:** Rollback tidak pernah diuji sebelum insiden; skrip kedaluwarsa
atau tidak kompatibel dengan versi terbaru; ketergantungan tersembunyi membuat
rollback satu layanan memicu kegagalan berantai. Mitigasi: jadwalkan drill rollback
kuartalan, sertakan rollback dalam definition-of-done setiap rilis besar.
"""  # noqa: E501

version = "0.0.1"
