"""Knowledge: Alert triage and prioritization procedures."""

title: str = "Prosedur Triage dan Prioritisasi Alert"

content: str = """
Triage alert menentukan urgency dan next action. Alert yang tidak ditriase dengan baik
menyebabkan alert fatigue dan missed incidents.

**Urgency Levels:** Critical (intervensi segera), High (dalam jam), Medium (dalam hari),
Low (informasional). Gunakan matriks impact vs urgency.

**Langkah Triage:** Konfirmasi alert bukan false positive; tentukan scope (satu tenant
atau seluruh platform); identifikasi apakah ada workaround; assign ke pemilik yang tepat.

**Reducing Noise:** Gabungkan alert terkait; gunakan aggregation window; review dan
tune threshold secara berkala. Dokumentasikan setiap alert dan rationale-nya.
"""  # noqa: E501

version: str = "0.0.1"
