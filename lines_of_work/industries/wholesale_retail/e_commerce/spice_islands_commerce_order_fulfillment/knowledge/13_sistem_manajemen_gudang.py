title = "Sistem Manajemen Gudang (WMS)"

content = """
WMS (Warehouse Management System) adalah perangkat lunak yang mengelola operasi
gudang: penerimaan barang, put-away, picking, packing, shipping, dan
inventori. Integrasi WMS dengan sistem pesanan dan kurir penting untuk
fulfillment yang akurat dan efisien.

**Fungsi Inti:** Pencatatan lokasi setiap SKU, penunjukan lokasi untuk
put-away baru, generasi pick list berdasarkan algoritma routing, pembaruan
stok real-time setelah setiap gerakan, dan pelaporan. WMS modern mendukung
mobile device untuk scanning barcode di lantai gudang.

**Integrasi:** WMS menerima pesanan dari OMS (Order Management System) atau
marketplace API. Setelah barang dikirim, WMS mengirim konfirmasi dan nomor
resi kembali ke sistem pesanan. Sinkronisasi dua arah menjaga konsistensi
data.

**Pemilihan WMS:** Sesuaikan dengan skala operasi. Startup kecil mungkin
menggunakan modul inventori di platform e-commerce; operasi besar membutuhkan
WMS dedicated seperti SAP EWM, Oracle WMS, atau solusi cloud.
"""  # noqa: E501

version = "0.0.1"
