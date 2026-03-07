"""Size ratio planning for production and cutting."""

title = "Perencanaan Rasio Ukuran"

content = """
Rasio ukuran menentukan distribusi quantity per size dalam satu order. Perencanaan
harus memastikan rasio sesuai PO dan meminimalkan sisa potongan.

**Sumber rasio:** PO customer, size curve historis, atau standar kategori. Gunakan
rasio yang disetujui customer untuk order ekspor.

**Cutting implication:** Rasio mempengaruhi marker dan fabric consumption. Rasio
tidak standar bisa meningkatkan waste. Diskusikan dengan cutting jika rasio ekstrem.

**Flexibility:** Beberapa customer mengizinkan deviasi ±5% per size. Catat dalam
order notes dan gunakan untuk optimasi cutting.
"""  # noqa: E501

version = "0.0.1"
