"""Knowledge item: standar dokumentasi test case."""

title = "Standar Dokumentasi Test Case"

content = """
Test case yang terdokumentasi dengan baik memungkinkan reproduksi, pelacakan cakupan,
dan onboarding anggota tim baru. Standar yang konsisten mengurangi ambiguitas dan
mempercepat eksekusi pengujian.

**Konteks:** Tim QA Pulau Data bekerja dengan berbagai klien dan proyek. Dokumentasi
standar memastikan bahwa test case dapat dipahami oleh pengembang, manajer proyek,
dan auditor tanpa konteks tambahan.

**Langkah Utama:**
1) Gunakan format seragam: ID, judul, prekondisi, langkah, data uji, hasil yang diharapkan.
2) Sertakan ID kebutuhan atau user story yang terkait untuk pelacakan cakupan.
3) Pisahkan test case positif dan negatif secara eksplisit.
4) Gunakan data uji yang representatif: nilai batas, nilai kosong, karakter khusus.
5) Perbarui dokumentasi saat kebutuhan atau perilaku berubah.

**Kriteria Penerimaan:** Test case dapat dieksekusi oleh anggota tim lain tanpa
klarifikasi. Cakupan kebutuhan dapat ditelusuri dari kebutuhan ke test case.

**Kegagalan Umum:** Dokumentasi terlalu ringkas sehingga tidak dapat direproduksi,
mengabaikan skenario negatif, atau tidak memperbarui test case setelah perubahan fitur.
"""

version = "0.0.1"
