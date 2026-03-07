"""Sewing line capacity planning."""

title = "Kapasitas Lini Jahit"

content = """
Kapasitas lini jahit diukur dalam unit per hari atau per shift. Output bergantung pada
jumlah operator, efisiensi lini, dan kompleksitas gaya. Gaya dengan banyak operasi dan
jahitan dekoratif menghasilkan output lebih rendah per operator.

**Standard allowed minute (SAM):** Setiap operasi memiliki SAM yang mendefinisikan waktu
standar. Total SAM per unit dibagi dengan jam kerja dan efisiensi target menghasilkan
kapasitas harian. Efisiensi aktual bervariasi dengan pengalaman operator dan kualitas
bahan.

**Bottleneck operasi:** Operasi dengan SAM tertinggi membatasi throughput. Line balancing
mendistribusikan kerja agar tidak ada stasiun yang overload.
"""  # noqa: E501

version = "0.0.1"
