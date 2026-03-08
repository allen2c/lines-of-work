"""Akurasi peramalan dan dampaknya pada rantai pasok."""

title = "Akurasi Peramalan"

content = """
Forecast accuracy mengukur seberapa dekat peramalan dengan actual. Metrik umum:
MAPE (Mean Absolute Percentage Error), bias, atau hit rate. Akurasi rendah menyebabkan
baik overstock maupun shortage — keduanya costly.

**Faktor**: Variabilitas demand, horizon panjang, dan perubahan tidak terantisipasi
mengurangi akurasi. Collaborative planning dengan sales dan production dapat improve.
Shorter horizon biasanya lebih akurat.

**Koordinasi**: Share forecast dengan pemasok; pastikan konsisten dengan internal
plan. Monitor accuracy; perbaiki process jika bias konsisten. Safety stock compensates
untuk uncertainty tetapi bukan pengganti perbaikan forecast.
"""  # noqa: E501

version = "0.0.1"
