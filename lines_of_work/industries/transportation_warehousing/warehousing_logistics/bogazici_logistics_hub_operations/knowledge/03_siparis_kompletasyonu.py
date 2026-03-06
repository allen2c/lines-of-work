title = "Sipariş Kompletasyonu"

content = """
Kompletasyon, müşteri siparişlerinin toplanması ve paketlenmeye hazır hale
getirilmesidir. Boğaziçi Hub'da tek sipariş (discrete) ve toplu (batch)
kompletasyon modları kullanılır.

**Tek Sipariş:** Bir sipariş tek kompletör tarafından toplanır. Küçük siparişler
ve acil gönderiler için uygundur.

**Toplu Kompletasyon:** Birden fazla sipariş aynı turda toplanır; paketleme
istasyonunda ayrıştırılır. Verimlilik yüksek, büyük hacimlerde tercih edilir.

**WMS Yönlendirmesi:** Sistem en kısa rota algoritması ile toplama sırası
belirler. Barkod tarama her adımda doğrulama sağlar.

**Hata Yönetimi:** Eksik stok durumunda sistem alternatif lokasyon önerir veya
kısmı sevkiyat onayı ister. Tüm aksaklıklar kayıt altına alınır.
"""  # noqa: E501

version = "0.0.1"
