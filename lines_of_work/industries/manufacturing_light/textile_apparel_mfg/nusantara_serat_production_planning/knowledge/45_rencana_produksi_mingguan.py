"""Weekly production plan."""

title = "Rencana Produksi Mingguan"

content = """
Rencana produksi mingguan memetakan alokasi order ke lini dan hari dalam satu
minggu. Rencana ini lebih detail daripada MPS bulanan dan menjadi acuan operasional.

**Struktur:** Setiap lini mendapat alokasi order per hari. Urutan produksi
mempertimbangkan prioritas, pergantian gaya, dan ketersediaan bahan. Buffer
disediakan untuk order darurat.

**Review:** Rencana mingguan direview setiap Jumat untuk minggu berikutnya.
Perubahan order, keterlambatan bahan, atau masalah produksi memicu revisi.

**Komunikasi:** Rencana final disebarkan ke supervisor, cutting, dan logistik
sebelum minggu dimulai.
"""  # noqa: E501

version = "0.0.1"
