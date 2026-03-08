"""Reorder point dan titik pemesanan ulang."""

title = "Reorder Point"

content = """
Reorder point (ROP) adalah tingkat inventori di mana pemesanan baru harus dilepas agar
stok tidak habis sebelum kedatangan. ROP = (daily demand × lead time in days) + safety
stock.

**Aplikasi**: Dalam sistem min-max atau reorder-point, ketika on-hand + on-order turun
di bawah ROP, release PO atau production order. Ukuran lot bisa tetap (EOQ) atau
dinamis (lot-for-lot untuk MRP).

**Pemantauan**: Lead time dan demand berubah. Review ROP periodik; gunakan data aktual
bukan asumsi. Items dengan demand tidak teratur mungkin perlu policy berbeda.
"""  # noqa: E501

version = "0.0.1"
