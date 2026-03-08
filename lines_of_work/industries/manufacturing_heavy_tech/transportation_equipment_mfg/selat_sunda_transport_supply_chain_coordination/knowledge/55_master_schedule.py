"""Master production schedule dan koordinasi dengan pengadaan."""

title = "Master Schedule"

content = """
Master production schedule (MPS) mendefinisikan apa yang akan diproduksi dan kapan.
MPS adalah input utama untuk MRP — dari MPS diturunkan kebutuhan material.
Perubahan MPS langsung berdampak pada pengadaan.

**Koordinasi**: Production planning owns MPS. Tim pengadaan harus aware perubahan
signifikan: acceleration, slowdown, model mix change. Setiap change trigger MRP
run dan potential PO adjustment. Communicate dengan pemasok untuk delivery date
changes.

**Frozen period**: MPS sering memiliki frozen period (1–2 weeks) di mana change
tidak allowed untuk stabilitas. Beyond frozen, flexibilitas ada tetapi dengan
lead time constraint.
"""  # noqa: E501

version = "0.0.1"
