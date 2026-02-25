title = "Idempotensi dalam Operasi Integrasi"

content = """
Operasi idempoten menghasilkan efek yang sama jika dieksekusi sekali atau berkali-kali.
Esensial dalam integrasi terdistribusi di mana retry, duplikasi jaringan, dan replikasi
dapat menyebabkan eksekusi ganda.

**Mengapa Penting:** Klien tidak bisa selalu mengetahui apakah permintaan sampai. Retry
setelah timeout bisa mengakibatkan duplikasi. Tanpa idempotensi: double charge, double
order, inconsistent state. Dengan idempotensi: aman untuk retry; sistem mencapai konsistensi.

**Implementasi:** Idempotency key: klien mengirim header Idempotency-Key dengan nilai unik
( UUID ). Server menyimpan key dan respons; permintaan ulang dengan key sama mengembalikan
respons tersimpan tanpa menjalankan ulang. Untuk update: PUT dengan id dan payload penuh
sering idempoten. CREATE memerlukan deduplikasi eksplisit.

**Design:** GET, PUT, DELETE alamiah idempoten. POST dan PATCH memerlukan perhatian khusus.
Dokumentasikan key dalam API; konsumen harus menghasilkan dan menyimpan key untuk retry.
"""  # noqa: E501

version = "0.0.1"
