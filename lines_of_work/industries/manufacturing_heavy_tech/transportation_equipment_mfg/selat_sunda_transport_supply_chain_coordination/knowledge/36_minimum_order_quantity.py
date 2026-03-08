"""Minimum order quantity dan dampaknya pada inventori."""

title = "Minimum Order Quantity"

content = """
Minimum order quantity (MOQ) adalah jumlah terkecil yang dapat dipesan dari pemasok.
Pemasok menetapkan MOQ untuk efisiensi produksi. MOQ tinggi dapat menyebabkan
overstock jika kebutuhan periodik lebih kecil dari MOQ.

**Strategi**: Negosiasi MOQ lebih rendah dengan strategic sourcing; kombinasi
beberapa part dalam satu order jika pemasok allow; terima lot besar dan consume
over time; cari alternatif pemasok dengan MOQ lebih fleksibel.

**Koordinasi**: Saat release PO, pastikan quantity memenuhi MOQ. Kuantitas di bawah
MOQ dapat ditolak atau dikenakan biaya tambahan.
"""  # noqa: E501

version = "0.0.1"
