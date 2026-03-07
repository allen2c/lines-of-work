"""Knowledge item: alur pengguna end-to-end."""

title = "Alur Pengguna End-to-End"

content = """
Pengujian end-to-end (E2E) memverifikasi alur pengguna lengkap dari perspektif pengguna
akhir. Ini adalah lapisan kepercayaan tertinggi sebelum rilis ke produksi.

**Konteks:** Untuk e-commerce, fintech, atau layanan kesehatan, alur seperti pendaftaran,
checkout, atau pemesanan janji adalah kritis. Kegagalan di sini langsung memengaruhi
pengguna dan reputasi bisnis. E2E memastikan seluruh rantai berfungsi bersama.

**Desain Skenario:**
- Pilih alur bisnis paling kritis (happy path dan beberapa edge case).
- Simulasi pengguna nyata: login, navigasi, input data, verifikasi hasil.
- Gunakan data uji yang realistis tetapi terisolasi (tidak memengaruhi produksi).

**Alat:** Selenium, Playwright, Cypress untuk web; Appium untuk mobile. Jalankan E2E
sebelum rilis atau pada jadwal terbatas karena mahal dan lambat.

**Kegagalan Umum:** Terlalu banyak skenario E2E (build sangat lambat), flaky test karena
ketergantungan waktu/jaringan, atau mengabaikan edge case kritis.
"""

version = "0.0.1"
