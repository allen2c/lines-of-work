"""Machine allocation for production lines."""

title = "Alokasi Mesin untuk Lini Produksi"

content = """
Alokasi mesin menentukan efisiensi dan throughput lini jahit. Di Nusantara Serat,
setiap mesin memiliki spesifikasi dan kapasitas yang berbeda. Jahit lurus, overlock,
buttonhole, dan mesin khusus harus dialokasikan sesuai kebutuhan operasi per gaya.

**Pemetaan operasi:** Setiap operasi jahit dalam tech pack dipetakan ke tipe mesin.
Operasi yang membutuhkan mesin khusus (misalnya bordir, quilting) dijadwalkan terlebih
dahulu karena ketersediaan terbatas.

**Rotasi dan perawatan:** Alokasi memperhitungkan jadwal perawatan preventif. Mesin
yang sama tidak boleh dialokasikan ke dua gaya bersamaan. Rotasi operator antar mesin
mengurangi kelelahan dan meningkatkan kualitas.
"""  # noqa: E501

version = "0.0.1"
