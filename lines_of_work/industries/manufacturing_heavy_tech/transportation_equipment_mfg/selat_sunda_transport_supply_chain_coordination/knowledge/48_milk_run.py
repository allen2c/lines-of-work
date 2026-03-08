"""Milk run dan pengiriman terjadwal multi-pemasok."""

title = "Milk Run"

content = """
Milk run adalah rute pengiriman terjadwal yang mengunjungi beberapa pemasok,
mengumpulkan barang, dan mengantarkan ke satu atau beberapa lokasi. Mengurangi
frekuensi truk individual dan mengoptimalkan utilisasi transport.

**Koordinasi**: Jadwal milk run harus fixed atau dengan window yang jelas. Pemasok
harus siap untuk pickup pada waktu yang ditentukan. Barang yang terlewat harus wait
until next run atau di-expedite terpisah.

**Manfaat**: Cost transport lebih rendah, lead time predictable, dan mengurangi
traffic di receiving dock. Cocok untuk pemasok lokalnya berdekatan atau dalam
kawasan industri.
"""  # noqa: E501

version = "0.0.1"
