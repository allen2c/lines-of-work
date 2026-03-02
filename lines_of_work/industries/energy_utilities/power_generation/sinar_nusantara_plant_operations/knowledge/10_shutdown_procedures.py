title = "Prosedur Shutdown"

content = """
Shutdown terencana dilakukan untuk pemeliharaan terjadwal atau saat grid tidak memerlukan
daya. Prosedur yang terkontrol melindungi peralatan dari stress termal dan mekanis.

**Urutan shutdown typical:**
Turunkan beban bertahap sesuai laju yang diizinkan. Lepas generator dari grid (de-sync)
kemudian trip turbin. Untuk combined cycle: steam turbin di-trip terlebih dahulu atau
mengikuti prosedur produsen; kemudian gas turbin. Biarkan peralatan mendingin (cooldown)
sesuai kurva yang ditentukan sebelum membuka atau mengakses.

**Cooling period:**
Gas turbin dan steam turbin memerlukan waktu cooldown untuk menghindari distorsi termal.
Jangan memaksa ventilasi atau membuka casing sebelum suhu turun ke batas aman. Rotasi
barring (jika tersedia) mencegah deflection rotor saat cooldown.

**Post-shutdown:**
Isolasi sistem bahan bakar. Pastikan sistem proteksi kebakaran aktif. Log semua parameter
saat trip dan langkah yang dilakukan. Lakukan inspeksi singkat bila diperlukan sebelum
menyerahkan ke tim pemeliharaan.
"""  # noqa: E501

version = "0.0.1"
