"""Audit pemasok dan proses kualifikasi."""

title = "Audit Pemasok"

content = """
Audit pemasok menilai kemampuan pemasok memenuhi persyaratan kualitas, delivery, dan
sistem manajemen. Biasanya dilakukan oleh QA atau third-party. Audit dapat
on-site atau remote (document review). Hasil: approved, conditional, atau reject.

**Koordinasi pengadaan**: Tim pengadaan tidak melakukan audit tetapi membutuhkan
hasil untuk release order. Pemasok belum approved tidak boleh supply production
material. Untuk conditional approval, pastikan action items diselesaikan.

**Periodic**: Re-audit sesuai schedule (misal tahunan) atau triggered oleh quality
issues. Maintain audit calendar.
"""  # noqa: E501

version = "0.0.1"
