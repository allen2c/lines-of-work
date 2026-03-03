title = "Kualitas Daya dan Stabilitas Grid"

content = """
Pembangkit harus menghasilkan listrik yang memenuhi standar kualitas PLN: tegangan, frekuensi,
harmonik, dan faktor daya dalam batas yang ditentukan. Ketidakpatuhan dapat mengakibatkan
penalti atau pemutusan dari grid.

**Parameter yang dipantau:**
Tegangan pada titik interkoneksi: harus dalam rentang ±5% dari nominal. Frekuensi: 50 Hz
±0.5 Hz normal. Faktor daya: biasanya 0.85–1.0 lagging sesuai perjanjian. Harmonik: THD
harus di bawah batas yang ditetapkan.

**Penyediaan daya reaktif:**
Generator dapat menghasilkan atau menyerap daya reaktif (MVAr) untuk mendukung tegangan grid.
P3B dapat meminta pembangkit untuk beroperasi dalam mode tertentu (mis. batas MVAr minimum)
untuk stabilitas transmisi.

**Fault ride-through:**
Pembangkit harus mampu tetap terhubung (tidak trip) selama gangguan grid transient tertentu
sesuai grid code PLN, agar tidak memperburuk gangguan. Durasi dan kedalaman gangguan
ditentukan dalam peraturan.
"""  # noqa: E501

version = "0.0.1"
