"""Shift scheduling for multi-shift operations."""

title = "Penjadwalan Shift"

content = """
Operasi multi-shift memaksimalkan utilisasi mesin dan ruang. Penjadwalan shift
harus memastikan kontinuitas produksi dan keseimbangan beban kerja.

**Shift Pattern:** Pola umum: 2 shift (06:00-14:00, 14:00-22:00) atau 3 shift
untuk operasi 24 jam. Pilih berdasarkan permintaan dan ketersediaan tenaga kerja.

**Handover antar Shift:** Setiap shift harus menerima informasi WIP, target,
dan masalah dari shift sebelumnya. Dokumentasi handover mencegah kehilangan konteks.

**Rotasi dan Keseimbangan:** Rotasi pekerja antar shift untuk keadilan dan
pengurangan kelelahan. Hindari penumpukan pekerja berpengalaman di satu shift saja.

**Maintenance Window:** Jadwalkan perawatan mesin di antara shift atau saat
low production untuk meminimalkan downtime.
"""  # noqa: E501

version = "0.0.1"
