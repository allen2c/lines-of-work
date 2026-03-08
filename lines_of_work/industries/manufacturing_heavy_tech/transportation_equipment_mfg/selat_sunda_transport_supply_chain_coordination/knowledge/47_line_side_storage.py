"""Line-side storage dan pasokan ke lini perakitan."""

title = "Line-Side Storage"

content = """
Line-side storage menyimpan komponen dekat titik penggunaan di lini perakitan,
mengurangi perpindahan dan memungkinkan operator akses cepat. Ukuran line-side
terbatas — biasanya 1–2 shift consumption. Replenishment dari main warehouse atau
direct from supplier (milk run).

**Kanban**: Line-side sering menggunakan Kanban — ketika bin kosong, kartu trigger
replenishment. Ukuran bin dan jumlah Kartu disesuaikan dengan usage rate dan
frekuensi delivery.

**Koordinasi**: Pastikan replenishment schedule selaras dengan production schedule.
Shortage di line-side = line stop. Monitor min-max levels dan adjust.
"""  # noqa: E501

version = "0.0.1"
