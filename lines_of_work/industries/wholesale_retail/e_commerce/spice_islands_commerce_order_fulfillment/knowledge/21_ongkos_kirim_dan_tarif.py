title = "Ongkos Kirim dan Perhitungan Tarif"

content = """
Ongkos kirim memengaruhi keputusan pembelian. Sistem yang akurat menghitung
tarif berdasarkan berat, dimensi, jarak, dan layanan kurir sehingga
pelanggan melihat estimasi yang benar saat checkout.

**Formula Dasar:** Tarif = f(berat, dimensi, zona, layanan). Kurir biasanya
menggunakan berat aktual atau berat volumetrik (panjang × lebar × tinggi /
divisor)—yang lebih besar dipakai. Zona ditentukan oleh kabupaten/kota
tujuan; Jawa umumnya lebih murah daripada Papua.

**Integrasi Cek Ongkir:** Marketplace dan website mengintegrasikan API cek
ongkir kurir. Pastikan dimensi dan berat produk di katalog akurat—kesalahan
menyebabkan selisih biaya yang harus ditanggung penjual atau pelanggan.

**Gratis Ongkir:** Banyak penjual menawarkan gratis ongkir di atas nilai
tertentu. Sistem harus mendeteksi eligible dan meniadakan charge ongkir
secara otomatis.
"""  # noqa: E501

version = "0.0.1"
