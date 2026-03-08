"""Sistem Kanban untuk pengadaan inbound."""

title = "Kanban Inbound"

content = """
Kanban inbound menggunakan sinyal visual atau elektronik untuk memicu pengisian ulang
bahan dari pemasok. Ketika inventori di line-side atau supermarket turun ke titik
tertentu, kartu Kanban dikirim ke pemasok atau tim pengadaan untuk release order.

**Jenis**: Two-bin Kanban (dua wadah bergantian), atau Kanban dengan jumlah kartu
tertentu yang beredar. Ukuran lot dan frekuensi pengisian disesuaikan dengan usage rate
dan lead time.

**Koordinasi**: Pastikan pemasok memahami sistem Kanban dan lead time. Monitor cycle
time; jika kartu menumpuk atau kosong, sesuaikan jumlah Kartu atau ukuran lot.
"""  # noqa: E501

version = "0.0.1"
