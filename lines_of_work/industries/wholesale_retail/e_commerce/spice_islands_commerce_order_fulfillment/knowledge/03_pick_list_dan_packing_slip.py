title = "Pick List dan Packing Slip"

content = """
Pick list dan packing slip adalah dokumen operasional yang memandu personel
gudang dari picking hingga pengemasan. Keduanya harus jelas, akurat, dan
mengurangi kesalahan manual.

**Pick List:** Daftar barang yang harus diambil dari lokasi penyimpanan,
biasanya disusun berdasarkan zona atau urutan aisle untuk meminimalkan jarak
tempuh. Setiap baris mencantumkan SKU, jumlah, lokasi (bin/slot), dan deskripsi
singkat. Pick list dapat digabung untuk batch picking jika beberapa pesanan
membutuhkan item yang sama.

**Packing Slip:** Dokumen yang ditempel atau dimasukkan ke dalam paket,
berisi ringkasan pesanan: daftar barang, jumlah, nama penerima, dan alamat.
Tidak termasuk informasi harga. Pelanggan menggunakan packing slip untuk
memverifikasi isi paket saat sampai.

**Integrasi dengan WMS:** Kedua dokumen dihasilkan oleh sistem manajemen gudang
dan terkait dengan nomor pesanan. Scanning barcode pada setiap langkah
memperbarui status pesanan secara real-time.
"""  # noqa: E501

version = "0.0.1"
