"""Bill of materials dan dampaknya pada pengadaan."""

title = "Persyaratan BOM"

content = """
Bill of materials (BOM) mendefinisikan komponen yang dibutuhkan per unit produk.
BOM digunakan oleh MRP untuk menurunkan kebutuhan ke level komponen. BOM yang salah
menyebabkan over atau under ordering.

**Koordinasi**: Pastikan BOM di ERP akurat dan up-to-date. Engineering change dapat
mengubah BOM; pastikan effectivity date dipahami. Untuk phase-in/phase-out, BOM
dapat memiliki multiple revisions active. Work dengan production planning untuk
alignment.

**Multi-level**: BOM dapat hierarchical (assembly → subassembly → component).
Lead time dan procurement strategy may vary by level.
"""  # noqa: E501

version = "0.0.1"
