title = "Clash Detection"

content = """
Clash detection mengidentifikasi tumpang tindih fisik antara elemen model (arsitek, struktur,
MEP). Hard clash: konflik yang mencegah konstruksi (duct melalui beam). Soft clash: clearance
tidak memadai untuk maintenance. Clash detection biasanya dijalankan di Navisworks atau
BIM 360; atur tolerance (misalnya 25mm) untuk mengabaikan false positive minor. Hasil:
clash report dengan screenshot, lokasi, dan severity. Tim menetapkan resolution (siapa
menggeser apa) dan memverifikasi dalam model berikutnya.

Clash harus diselesaikan sebelum issue gambar IFC. Clash yang tertinggal menyebabkan
perubahan lapangan, RFI, dan claim. Jadwalkan clash run teratur selama design development
dan sebelum setiap major milestone.
"""  # noqa: E501

version = "0.0.1"
