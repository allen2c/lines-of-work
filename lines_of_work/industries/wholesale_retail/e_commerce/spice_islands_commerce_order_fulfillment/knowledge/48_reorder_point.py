title = "Reorder Point dan Titik Pemesanan Ulang"

content = """
Reorder point (ROP) adalah tingkat stok yang memicu pemesanan ulang ke
supplier. Ketika stok turun ke atau di bawah ROP, pesanan pembelian
dibuat untuk menjaga ketersediaan selama lead time.

**Rumus Sederhana:** ROP = (daily demand × lead time in days) + safety stock.
Contoh: demand 10 unit/hari, lead time 7 hari, safety stock 20 → ROP = 90.
Saat stok mencapai 90, pesan replenishment.

**Considerasi:** Lead time tidak selalu konstan; demand musiman. Beberapa
sistem menggunakan dynamic ROP yang menyesuaikan dengan tren demand.

**Integrasi dengan Fulfillment:** Ketika stok mendekati ROP, tim pembelian
harus proaktif. Stok habis sebelum restok tiba menyebabkan backorder
atau lost sales.
"""  # noqa: E501

version = "0.0.1"
