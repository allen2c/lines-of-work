title = "Penanganan Exception dalam Fulfillment"

content = """
Exception adalah kejadian di luar alur normal yang memerlukan intervensi
manual atau keputusan khusus. Contoh: stok tidak ditemukan, alamat
tidak valid, pembayaran dispute, atau barang rusak saat picking.

**Kategori Exception:** Stock exception (tidak ada di lokasi, selisih
jumlah), address exception (tidak dapat diverifikasi), payment exception
(chargeback, refund tertunda), dan quality exception (cacat saat packing).

**Prosedur:** Exception didokumentasikan dan di-assign ke tim yang
berwenang. Setiap tipe memiliki SOP resolusi—mis. stok tidak ada:
cek lokasi alternatif, substitute dengan persetujuan pelanggan, atau
cancel dan refund.

**Eskalasi:** Exception yang tidak terselesaikan dalam SLA harus
dieskalasi ke supervisor atau manajer.
"""  # noqa: E501

version = "0.0.1"
