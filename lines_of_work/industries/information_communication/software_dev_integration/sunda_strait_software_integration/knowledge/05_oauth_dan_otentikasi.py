title = "OAuth dan Otentikasi untuk Integrasi API"

content = """
Otentikasi aman adalah fondasi integrasi yang handal. OAuth 2.0 adalah standar dominan
untuk otorisasi delegasi — memungkinkan aplikasi mengakses sumber daya atas nama pengguna
tanpa membagikan kredensial.

**Grant Types:** Client Credentials untuk machine-to-machine (backend ke backend); paling
umum dalam integrasi B2B. Authorization Code untuk aplikasi dengan pengguna; melibatkan
redirect dan consent. Refresh token untuk memperpanjang akses tanpa login ulang.

**Best Practice:** Simpan token di tempat aman; jangan log atau masukkan ke kode. Refresh
sebelum kedaluwarsa. Gunakan scope seminimal mungkin. Validasi state dalam Authorization
Code flow untuk mencegah CSRF.

**API Keys vs OAuth:** API key sederhana untuk sandbox atau akses terbatas. OAuth untuk
produksi ketika akses perlu dibatasi per scope, dapat dicabut, dan diaudit. Kombinasi
keduanya (API key identifikasi, OAuth otorisasi) juga lazim.
"""  # noqa: E501

version = "0.0.1"
