title = "Safety Stock dan Buffer Inventori"

content = """
Safety stock adalah cadangan stok untuk menanggulangi ketidakpastian
permintaan atau supply. Buffer ini mengurangi risiko stockout saat
permintaan melonjak atau restok tertunda.

**Perhitungan Dasar:** Safety stock = (max daily demand - avg daily demand)
× lead time. Atau menggunakan formula statistik berdasarkan deviasi standar
demand dan lead time. Metode yang lebih canggih memakai simulasi atau
optimasi.

**Faktor:** Variabilitas permintaan, lead time supplier, criticality
produk (berapa penting tidak boleh kehabisan). Produk high-turnover
memerlukan safety stock lebih besar.

**Trade-off:** Safety stock tinggi menambah biaya holding dan risiko
obsolete. Balance antara ketersediaan dan efisiensi modal.
"""  # noqa: E501

version = "0.0.1"
