title = "Generator Listrik"

content = """
Generator sinkron mengubah energi putar dari turbin menjadi listrik AC tiga fasa. Di Sinar
Nusantara, dua gas turbin dan satu steam turbin masing-masing terhubung ke generator sendiri.

**Prinsip operasi:**
Rotor berputar dalam medan magnet stator; induksi elektromagnetik menghasilkan tegangan AC.
Frekuensi keluaran (50 Hz di Indonesia) harus sesuai dengan frekuensi grid PLN. Excitation
system mengontrol tegangan keluaran dengan mengatur arus DC pada rotor.

**Parameter yang dipantau:**
Tegangan, arus, daya aktif (MW), daya reaktif (MVAr), faktor daya, frekuensi, dan suhu
windings. Batas panas ditentukan oleh kelas isolasi; operasi berkelanjutan di atas batas
mengurangi umur peralatan.

**Sinkronisasi ke grid:**
Sebelum menghubungkan generator ke grid, fase, frekuensi, dan tegangan harus sinkron dengan
grid. Auto-synchronizer (jika ada) atau prosedur manual harus diikuti dengan ketat. Salah
sinkronisasi dapat merusak generator dan peralatan grid.
"""  # noqa: E501

version = "0.0.1"
