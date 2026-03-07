"""Penyeimbangan lini jahit untuk aliran produksi optimal."""

title = "Line Balancing"

content = """
Line balancing mendistribusikan operasi jahit ke stasiun kerja sehingga waktu siklus
per stasiun mendekati sama. Ketidakseimbangan menyebabkan menunggu dan bottleneck.

**SMV per Operasi:** Setiap operasi memiliki SMV. Total SMV dibagi jumlah operator
memberikan target output per jam. Stasiun dengan SMV tertinggi menjadi bottleneck.

**Strategi:** Gabungkan operasi kecil, pecah operasi besar, atau tambahkan operator
di bottleneck. Tujuan: variasi waktu siklus antar stasiun kurang dari 15%.

**Ulangi saat Gaya Baru:** Setiap gaya baru memerlukan line balancing ulang karena
urutan dan kompleksitas operasi berbeda.
"""  # noqa: E501

version = "0.0.1"
