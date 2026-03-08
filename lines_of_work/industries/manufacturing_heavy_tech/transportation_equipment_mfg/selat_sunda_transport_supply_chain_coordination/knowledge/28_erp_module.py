"""Modul ERP untuk pengadaan dan inventori."""

title = "Modul ERP Pengadaan"

content = """
Modul pengadaan dalam ERP umumnya meliputi: purchase requisition, purchase order,
goods receipt, invoice verification, dan vendor master. Modul inventori mengelola
stock levels, movements, dan valuations.

**Workflow**: Requisition → approval → PO creation → PO release → receipt → invoice
match → payment. Setiap tahap terdokumentasi di sistem untuk audit trail.

**Koordinasi**: Pastikan data master (vendor, item, UOM) akurat. Gunakan approval
workflow sesuai policy. Integration dengan WMS untuk put-away dan picking.
"""  # noqa: E501

version = "0.0.1"
