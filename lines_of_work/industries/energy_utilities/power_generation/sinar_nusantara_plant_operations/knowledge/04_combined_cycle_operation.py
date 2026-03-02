title = "Operasi Combined Cycle"

content = """
Sinar Nusantara menggunakan siklus kombinasi: gas turbin menghasilkan listrik sekaligus
memanaskan gas buang. Gas buang ini digunakan di HRSG untuk menghasilkan uap yang menggerakkan
steam turbin generator, sehingga efisiensi total lebih tinggi daripada PLTU berbahan bakar
gas saja.

**Alur energi:**
Gas alam dibakar di gas turbin; sebagian energi dikonversi menjadi listrik, sisanya dalam
bentuk panas gas buang. HRSG memindahkan panas dari gas buang ke air untuk menghasilkan
uap bertekanan tinggi dan suhu tinggi. Steam turbin mengubah energi uap menjadi listrik
tambahan.

**Koordinasi gas-steam:**
Beban steam turbin mengikuti output gas turbin. Saat gas turbin menurunkan beban atau trip,
steam turbin juga akan terdampak. Perhatikan delay termal antara perubahan gas turbin dan
respons HRSG-steam turbin.

**Mode operasi:**
Pembangkit dapat beroperasi dalam mode combined cycle (gas + steam) atau mode simple cycle
(hanya gas turbin) jika steam turbin atau HRSG dalam pemeliharaan. Simple cycle memiliki
efisiensi lebih rendah tetapi memberikan fleksibilitas.
"""  # noqa: E501

version = "0.0.1"
