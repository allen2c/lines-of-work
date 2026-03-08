"""Kapasitas pemasok dan manajemen bottleneck."""

title = "Kapasitas Pemasok"

content = """
Kapasitas pemasok adalah kemampuan produksi maksimal dalam periode tertentu.
Keterbatasan kapasitas dapat membatasi kemampuan memenuhi demand spike atau
recovery dari shortage. Capacity constraint adalah root cause banyak delivery
issues.

**Koordinasi**: Share rolling forecast dengan pemasok agar mereka dapat plan
capacity. Untuk peak demand atau new program, early discussion untuk capacity
commitment. Jika pemasok capacity-limited, consider second source atau buffer
stock. Eskalasi ke strategic sourcing untuk capacity negotiation.

**Signals**: Repeated late delivery, partial shipments, atau reluctance to
commit mungkin indicate capacity issue.
"""  # noqa: E501

version = "0.0.1"
