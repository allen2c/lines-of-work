"""Knowledge item: validasi input dan sanitasi."""

title = "Validasi Input dan Sanitasi"

content = """
Validasi input dan sanitasi mencegah cacat keamanan dan perilaku tak terduga akibat data
masukan yang salah format, berbahaya, atau jahat. Fondasi keamanan aplikasi.

**Konteks:** Aplikasi web dan API menerima input dari pengguna, sistem eksternal, dan
file upload. Input yang tidak divalidasi dapat menyebabkan injeksi SQL, XSS, atau
kerusakan data. UU PDP Indonesia menuntut perlindungan data pribadi.

**Langkah Utama:**
1) Validasi tipe, format, panjang, dan rentang nilai di lapisan input.
2) Sanitasi output untuk mencegah XSS dan injeksi.
3) Gunakan whitelist, bukan blacklist, untuk aturan validasi.
4) Uji dengan payload berbahaya (OWASP Top 10) dalam test case.
5) Dokumentasikan aturan validasi dan tangani error dengan pesan yang aman.

**Kriteria Penerimaan:** Semua titik input kritis divalidasi, test keamanan otomatis
ada, dan kegagalan validasi ditangani tanpa mengekspos informasi sensitif.

**Kegagalan Umum:** Validasi hanya di frontend, mengabaikan API, atau pesan error
mengungkapkan detail internal.
"""

version = "0.0.1"
