"""Proses dan unsur purchase order yang valid."""

title = "Purchase Order"

content = """
Purchase order (PO) adalah dokumen resmi yang mengikat pembeli dan pemasok. PO harus
memuat: nomor PO, tanggal, kode dan deskripsi item, kuantitas, harga satuan, tanggal
pengiriman yang diinginkan, incoterms, dan syarat pembayaran.

**Proses**: Setelah kebutuhan terkonfirmasi dari MRP atau manual request, buat PO dan
kirim ke pemasok. Pemasok mengembalikan acknowledgment; jika ada perbedaan tanggal atau
kuantitas, segera koordinasikan dan perbarui sistem. Simpan semua versi PO untuk audit.

**Best practice**: Pastikan PO sesuai dengan kontrak master bila ada. Jangan mengubah
harga atau syarat tanpa persetujuan strategic sourcing. Gunakan blanket PO untuk
pengadaan berulang dengan release schedule.
"""  # noqa: E501

version = "0.0.1"
