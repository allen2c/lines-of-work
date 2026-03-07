"""
Knowledge item 09: integration point mapping. Documents all service boundaries
and data flows for reliability planning.
"""

title = "integration point mapping"

content = """
Entegrasyon noktası haritalama, tüm servis sınırlarını ve veri akışlarını
belgeleyerek güvenilirlik planlamasını destekler. Görünürlük olmadan bağımlılık
analizi ve hata izolasyonu yapılamaz.

**Bağlam:** Bosphorus Strait mimarilerinde onlarca mikroservis ve harici API
bulunabilir. Her entegrasyon noktası potansiyel başarısızlık kaynağıdır.

**Temel prosedürler:**
1) Tüm senkron ve asenkron entegrasyonları listeleyin: REST, gRPC, mesaj kuyrukları.
2) Her nokta için sağlayıcı, tüketici, protokol ve SLA bilgilerini kaydedin.
3) Bağımlılık grafiği oluşturun; tek nokta arızası (SPOF) ve darboğazları tespit edin.
4) Değişikliklerde haritayı güncelleyin; mimari incelemelerde referans alın.
5) Haritayı otomatik keşif araçları ile doğrulayın; sürüklenmeyi önleyin.

**Kabul kriterleri:** Harita güncel, tüm kritik akışlar kapsanmış ve SPOF'lar
belirlenmiş olduğunda etkin sayılır.
"""  # noqa: E501

version = "0.0.1"
