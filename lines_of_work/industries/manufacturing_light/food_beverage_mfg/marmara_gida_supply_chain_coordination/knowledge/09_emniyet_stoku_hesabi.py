"""Knowledge: Emniyet stoku hesaplama ve yönetimi."""

title = "Emniyet Stoku Hesaplama"

content = """
Emniyet stoku, talep veya tedarik belirsizliğine karşı tutulan ek stoktur.
Temel formül: ortalama günlük tüketim × gecikme günü + talep sapması payı.
Lead time değişkenliği ve talep tahmin hatası dikkate alınır. Kritik
hammaddelerde emniyet stoku yüksek tutulur; raf ömrü kısa ürünlerde düşük.
Periyodik (aylık/çeyreklik) gözden geçirme yapılır. Aşırı stok maliyet
ve bozulma riski getirir.
"""  # noqa: E501

version = "0.0.1"
