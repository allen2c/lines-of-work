"""Knowledge: Incident management workflow and escalation."""

title: str = "Alur Kerja Manajemen Insiden"

content: str = """
Manajemen insiden mengikuti siklus detect, respond, resolve, dan learn.

**Deteksi:** Alert dari sistem pemantauan, pelaporan pelanggan, atau observasi proaktif.
Klasifikasikan severity: P1 (kritik), P2 (tinggi), P3 (medium), P4 (rendah).

**Response:** Assign incident commander. Komunikasi awal dalam 15 menit untuk P1/P2.
Gunakan war room atau channel khusus untuk koordinasi.

**Resolusi:** Identifikasi root cause, terapkan mitigasi atau rollback. Pastikan layanan
stabil sebelum menutup insiden.

**Learn:** Post-incident review (PIR) wajib untuk P1/P2 dalam 48–72 jam. Dokumentasikan
root cause, action items, dan langkah pencegahan.
"""  # noqa: E501

version: str = "0.0.1"
