title = "Pengelolaan Data Siswa"

content = """
- Data siswa disimpan dalam sistem database (MySQL) yang diakses melalui aplikasi internal "SiswaKu".
- Data yang dicatat: nama, NISN, sekolah, kelas, alamat, nomor telepon orang tua, riwayat nilai, dan kehadiran.
- Akses data dibatasi: koordinator dan admin dapat melihat semua data, tentor hanya dapat melihat data siswa yang diajar.
- Backup data dilakukan setiap hari pukul 23.00 ke cloud (Google Drive) dan hard disk eksternal.
- Jika ada permintaan perubahan data (misal alamat), orang tua harus mengisi formulir perubahan dan diverifikasi dengan panggilan telepon.
"""

version = "0.0.1"
