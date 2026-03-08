"""Prosedur penerimaan barang dan pemeriksaan dokumen."""

title = "Penerimaan Barang"

content = """
Penerimaan barang dimulai dengan verifikasi: truck/container sesuai pengiriman yang
dijadwalkan, jumlah karton/unit sesuai packing list, dan kondisi kemasan baik.
Periksa bill of lading, packing list, dan certificate of conformance bila ada.

**Proses**: Unload, hitung/scan item, bandingkan dengan PO dan packing list. Selisih
harus didokumentasikan (shortage, overage, damage). Masukkan receipt ke sistem ERP
untuk update inventori dan trigger pembayaran jika three-way match.

**Quality**: Bila incoming inspection diperlukan, pindahkan ke hold area sampai
dilepas QA. Jangan gunakan untuk produksi sebelum release.
"""  # noqa: E501

version = "0.0.1"
