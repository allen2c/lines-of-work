"""Knowledge item: standar pengujian unit."""

title = "Standar Pengujian Unit"

content = """
Pengujian unit memverifikasi bahwa unit kode terkecil berperilaku sesuai harapan. Standar
yang konsisten memastikan pengujian dapat dipelihara dan dipahami oleh seluruh tim.

**Konteks:** Di Pulau Data, pengujian unit dijalankan pada setiap commit melalui CI. Standar
yang jelas mengurangi debat tentang apa yang harus diuji dan bagaimana menulis assertion.

**Prinsip:**
- **Satu konsep per test:** Setiap test case memverifikasi satu perilaku.
- **AAA (Arrange-Act-Assert):** Struktur jelas: siapkan data, jalankan aksi, periksa hasil.
- **Nama deskriptif:** Nama test menjelaskan skenario dan hasil yang diharapkan.
- **Independen:** Test tidak bergantung pada urutan eksekusi atau status global.

**Alat:** pytest (Python), Jest (JavaScript/TypeScript), JUnit (Java) adalah pilihan umum.
Gunakan mock untuk dependensi eksternal agar test tetap cepat dan deterministik.

**Kegagalan Umum:** Test yang terlalu rapuh (gagal karena perubahan kecil), test yang
menguji implementasi bukan perilaku, atau test yang lambat karena mengakses jaringan/DB.
"""

version = "0.0.1"
