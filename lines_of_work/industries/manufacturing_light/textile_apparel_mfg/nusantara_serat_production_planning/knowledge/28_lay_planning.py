"""Lay planning for cutting room efficiency."""

title = "Perencanaan Lay"

content = """
Lay planning menentukan berapa lapis kain yang disusun dalam satu spread untuk
cutting. Mempengaruhi throughput cutting dan fabric utilization.

**Lay height:** Batas maksimal tergantung jenis kain dan mesin spreading. Kain
tebal (denim, canvas) biasanya 50–80 lapis; kain tipis bisa 100–200 lapis.

**Quantity alignment:** Sesuaikan jumlah lapis dengan quantity order dan marker
untuk meminimalkan sisa. Hitung: lapis × pieces per lay = total pieces.

**Spreading direction:** Perhatikan nap, pattern direction, dan grain. Salah
arah bisa menyebabkan reject seluruh lay.
"""  # noqa: E501

version = "0.0.1"
