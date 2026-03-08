"""Knowledge: On-call response expectations and practices."""

title: str = "Ekspektasi dan Praktik On-Call Response"

content: str = """
On-call adalah tanggung jawab operasional untuk merespons insiden di luar jam kerja.
Praktik yang baik melindungi kesejahteraan engineer dan layanan.

**Response Time:** Target acknowledgment: 15 menit untuk P1, 30 menit untuk P2.
Definisi jelas dalam runbook dan kontrak on-call.

**Best Practice:** Handoff dokumentasikan konteks aktif; batasi jam on-call per orang;
compensate dengan time-off atau uang. Hindari single person sebagai bottleneck.

**Alat:** PagerDuty, Opsgenie, atau similar untuk alert routing dan escalation.
Integrasi dengan Slack/Teams untuk notifikasi cepat.
"""  # noqa: E501

version: str = "0.0.1"
