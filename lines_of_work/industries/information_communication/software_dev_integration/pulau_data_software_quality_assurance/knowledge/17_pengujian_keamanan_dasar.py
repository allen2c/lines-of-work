"""Knowledge item: pengujian keamanan dasar."""

title = "Pengujian Keamanan Dasar"

content = """
Pengujian keamanan dasar mencakup validasi autentikasi, otorisasi, manajemen rahasia,
dan sanitasi input. Untuk aplikasi yang menangani data pribadi atau transaksi keuangan,
pengujian keamanan adalah bagian wajib dari siklus QA.

**Konteks:** UU PDP Indonesia dan standar industri (PCI-DSS untuk pembayaran) menuntut
bukti bahwa data dilindungi. Celah keamanan yang lolos ke produksi dapat mengakibatkan
denda, kehilangan kepercayaan, dan kerugian finansial.

**Langkah Utama:**
1) Verifikasi autentikasi: login, logout, sesi kedaluwarsa, penguncian akun.
2) Verifikasi otorisasi: akses berdasarkan peran, batasan endpoint per pengguna.
3) Periksa manajemen rahasia: tidak ada kredensial hardcode, variabel lingkungan aman.
4) Uji sanitasi input: SQL injection, XSS, validasi format input.
5) Dokumentasikan temuan dengan severity dan langkah reproduksi.

**Kriteria Penerimaan:** Semua vektor serangan umum telah diuji. Temuan kritis dan tinggi
ditutup sebelum rilis. Bukti pengujian terdokumentasi untuk audit.

**Kegagalan Umum:** Mengabaikan pengujian keamanan untuk rilis "kecil", tidak menguji
endpoint yang dianggap "internal", atau tidak memvalidasi ulang setelah perbaikan.
"""

version = "0.0.1"