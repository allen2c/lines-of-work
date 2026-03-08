"""Safety stock dan peranannya dalam rantai pasok."""

title = "Inventori Safety Stock"

content = """
Safety stock adalah buffer inventori untuk menyerap variabilitas permintaan dan lead time.
Tanpa safety stock, fluktuasi kecil dapat menyebabkan shortage dan line stop. Terlalu
banyak safety stock meningkatkan biaya simpan dan risiko obsolet.

**Perhitungan dasar**: Safety stock = Z × σ_demand × √(lead time) atau formula serupa
dengan variabilitas lead time. Z tergantung service level yang ditargetkan (misalnya
95% → Z ≈ 1.65).

**Review berkala**: Sesuaikan safety stock berdasarkan actual demand, lead time pemasok,
dan criticality item. Komponen dengan single-source atau lead time panjang biasanya
perlu safety stock lebih tinggi.
"""  # noqa: E501

version = "0.0.1"
