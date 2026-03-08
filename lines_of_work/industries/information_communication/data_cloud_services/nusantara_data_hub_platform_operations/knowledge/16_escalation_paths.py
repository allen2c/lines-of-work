"""Knowledge: Escalation paths and ownership matrix."""

title: str = "Jalur Eskalasi dan Matriks Kepemilikan"

content: str = """
Escalation path mendefinisikan siapa harus dihubungi dan kapan. Matriks kepemilikan
memperjelas tanggung jawab per domain.

**Tier 1:** Platform ops — insiden umum, alert, dukungan pelanggan dasar.
**Tier 2:** Engineering — bug, perubahan konfigurasi, deployment issues.
**Tier 3:** Architect/Security — desain, keamanan, compliance.

**On-Call:** Rotasi jelas; dokumentasi kontak dan handoff. Pastikan secondary
tersedia untuk escalation dari primary.

**Vendor Escalation:** Untuk insiden yang melibatkan cloud provider atau SaaS,
ikuti proses support vendor. Dokumentasikan ticket ID dan SLA response.
"""  # noqa: E501

version: str = "0.0.1"
