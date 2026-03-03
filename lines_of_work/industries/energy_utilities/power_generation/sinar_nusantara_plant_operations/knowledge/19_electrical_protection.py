title = "Proteksi Listrik"

content = """
Proteksi listrik mendeteksi gangguan (short circuit, overload, earth fault) dan memerintahkan
circuit breaker untuk memutus sirkuit, membatasi kerusakan dan melindungi peralatan serta
personel.

**Relay proteksi:**
Differential protection untuk generator dan transformator. Overcurrent dan earth fault untuk
feeder. Distance relay untuk transmisi. Setpoint dan kurva waktu (time-current) harus sesuai
dengan koordinasi selektif: hanya bagian yang terganggu yang trip, bukan seluruh sistem.

**Pengujian:**
Relay dan circuit breaker diuji berkala sesuai standar. Pastikan trip coil dan mekanisme
breaker berfungsi. Dokumen skema proteksi dan setpoint harus terkini.

**Kegagalan proteksi:**
Proteksi gagal trip: gangguan dapat merusak peralatan dan membahayakan. Proteksi salah trip:
gangguan kecil mematikan pembangkit tidak perlu. Keduanya merugikan; rawat sistem proteksi
dengan serius.
"""  # noqa: E501

version = "0.0.1"
