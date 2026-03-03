title = "Rekonsiliasi Inventori dan Stock Opname"

content = """
Rekonsiliasi membandingkan jumlah stok dalam sistem dengan stok fisik di
gudang. Selisih (variance) dapat terjadi karena kesalahan scanning, kerusakan
tidak tercatat, atau pencurian. Stock opname berkala menjaga akurasi data.

**Siklus Counting:** Beberapa gudang melakukan full stock opname tahunan;
lainnya memakai cycle counting—menghitung sebagian SKU secara bergiliran
setiap hari atau minggu. SKU bernilai tinggi atau high-turnover sering
dihitung lebih sering.

**Prosedur:** Personel menghitung barang fisik di lokasi, mencatat jumlah,
dan membandingkan dengan sistem. Variance dilaporkan, diselidiki, dan
disesuaikan. Root cause analysis untuk variance besar atau berulang.

**Dampak pada Fulfillment:** Selama stock opname, item tertentu mungkin
dikunci untuk picking. Rencanakan jadwal counting agar tidak mengganggu
peak season.
"""  # noqa: E501

version = "0.0.1"
