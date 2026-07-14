title = "Manajemen Aset Data Center"

content = """
- Semua aset (server, switch, PDU, UPS, CRAC) dicatat dalam database aset (AssetDB) dengan atribut: nomor seri, model, lokasi rak, tanggal pembelian, garansi, status.
- Setiap aset diberi label barcode yang dipindai saat pemasangan, pemindahan, atau penghapusan.
- Prosedur:
  - Pemasangan: buat tiket permintaan, daftarkan di AssetDB, tempel label, catat konsumsi daya.
  - Pemindahan: update lokasi di AssetDB, pastikan tidak ada kabel yang tertinggal.
  - Penghapusan (decommission): hapus data, format disk, catat tanggal penghapusan, dan serahkan ke vendor daur ulang.
- Audit aset dilakukan setiap 6 bulan dengan mencocokkan fisik dan database. Selisih harus diselidiki dan diperbaiki.
- Garansi: pantau masa garansi setiap bulan. Jika akan habis dalam 3 bulan, ajukan perpanjangan atau penggantian.
"""  # noqa: E501

version = "0.0.1"
