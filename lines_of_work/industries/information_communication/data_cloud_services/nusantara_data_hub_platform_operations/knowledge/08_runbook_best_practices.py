"""Knowledge: Runbook best practices for operational procedures."""

title: str = "Best Practice Runbook untuk Prosedur Operasional"

content: str = """
Runbook adalah dokumentasi prosedur operasional untuk menangani insiden dan tugas
rutin. Runbook yang baik mempercepat response dan mengurangi human error.

**Struktur:** Judul jelas; kondisi pemicu (kapan menjalankan); prerequisit; langkah
berurutan dengan perintah dan parameter; kriteria sukses; kontak escalation.

**Format:** Gunakan numbering, code blocks untuk perintah, dan screenshot untuk UI.
Hindari prosedur yang bergantung pada konteks tacit; jelaskan asumsi.

**Maintenance:** Review runbook setelah setiap insiden. Update ketika arsitektur atau
tooling berubah. Test runbook secara periodik.
"""  # noqa: E501

version: str = "0.0.1"
