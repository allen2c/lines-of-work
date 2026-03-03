title = "Trip dan Shutdown Darurat"

content = """
Sistem proteksi otomatis akan trip turbin dan generator ketika parameter kritis melewati
batas. Tujuan: melindungi manusia dan peralatan. Operator harus merespons dengan cepat dan
mengikuti prosedur pemulihan.

**Penyebab trip umum:**
Kelebihan kecepatan (overspeed), EGT tinggi, getaran tinggi, kehilangan pengapian (flame out),
kehilangan pelumas, kehilangan tekanan gas, gangguan listrik (under-voltage, fault),
proteksi generator (differential, overcurrent). Setiap trip mencatat penyebab di DCS.

**Tindakan segera:**
Verifikasi peralatan dalam kondisi aman (turbin berhenti, bahan bakar terisolasi). Cek
apakah ada kebakaran, kebocoran gas, atau cedera. Aktifkan prosedur evakuasi bila perlu.
Laporkan ke P3B dan manajer pembangkit. Jangan mencoba restart sebelum penyebab ditentukan
dan disetujui.

**Investigasi:**
Catat waktu trip, parameter saat kejadian, dan alarm yang muncul. Simpan data log untuk
analisis. Jangan reset atau clear alarm sebelum dokumentasi lengkap.
"""  # noqa: E501

version = "0.0.1"
