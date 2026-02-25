title = "Dasar REST API untuk Integrasi"

content = """
REST (Representational State Transfer) adalah gaya arsitektur yang dominan untuk integrasi
berbasis HTTP. Memahami prinsip REST memastikan API yang konsisten dan dapat dipelihara.

**Sumber Daya dan Metode:** REST memodelkan data sebagai sumber daya yang diidentifikasi
oleh URI. Metode HTTP (GET, POST, PUT, PATCH, DELETE) memetakan operasi CRUD. GET untuk
membaca, POST untuk membuat, PUT/PATCH untuk memperbarui, DELETE untuk menghapus.

**Kode Status:** Gunakan kode status HTTP dengan benar. 200 untuk sukses, 201 untuk dibuat,
204 untuk sukses tanpa konten, 400 untuk permintaan salah, 401/403 untuk otentikasi/otorisasi,
404 untuk tidak ditemukan, 429 untuk rate limit, 500 untuk kesalahan server.

**Versioning:** Versi API melalui URI path (/v1/resource) atau header Accept. Konsistensi
penting; jangan campur kedua pendekatan dalam satu API. Rencanakan deprecation untuk versi lama.
"""  # noqa: E501

version = "0.0.1"
