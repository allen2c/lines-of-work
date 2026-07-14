title = "Rencana Pemulihan Bencana (DR)"

content = """
- DR site terletak di kota berbeda (Jakarta → Surabaya) dengan replikasi data asinkron.
- RTO (Recovery Time Objective) untuk layanan kritis: 4 jam. RPO: 1 jam.
- Skenario bencana: gempa bumi, kebakaran, pemadaman listrik total, serangan siber besar.
- Prosedur aktivasi DR:
  1. Manajer Operasi memutuskan aktivasi berdasarkan dampak.
  2. Tim operasi menjalankan runbook failover: alihkan DNS, aktifkan VM di DR, verifikasi koneksi.
  3. Komunikasikan ke pelanggan melalui email dan portal status.
  4. Setelah bencana selesai, lakukan failback secara bertahap.
- Uji DR dilakukan setiap 6 bulan dengan simulasi penuh. Hasil uji didokumentasikan dan diperbaiki.
"""  # noqa: E501

version = "0.0.1"
