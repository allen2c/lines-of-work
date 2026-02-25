title = "Pemetaan dan Transformasi Data"

content = """
Integrasi antar sistem sering memerlukan transformasi data antara format dan skema yang
berbeda. Pemetaan yang baik memastikan akurasi dan kemudahan pemeliharaan.

**Sumber ke Target:** Identifikasi field yang setara meskipun nama atau tipe berbeda.
Tanggal: ISO 8601 vs epoch vs format lokal. Mata uang: kode vs simbol, presisi desimal.
Null dan nilai default: definisikan perilaku untuk field kosong.

**Transformasi Umum:** Mapping 1:1, agregasi (banyak ke satu), pemecahan (satu ke banyak).
Validasi: format, range, referensi integritas. Enkripsi/dekripsi untuk data sensitif.

**Tool dan Pendekatan:** MapStruct, Jolt, atau kode ad-hoc. Untuk kompleksitas tinggi,
pertimbangkan ETL engine atau low-code integrator. Dokumentasikan aturan transformasi;
mereka cenderung berubah seiring evolusi sistem sumber dan target.
"""  # noqa: E501

version = "0.0.1"
