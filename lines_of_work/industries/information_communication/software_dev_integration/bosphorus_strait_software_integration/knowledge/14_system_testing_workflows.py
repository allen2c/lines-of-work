"""
Knowledge item 14: system testing workflows. End-to-end system behavior validation
across all layers.
"""

title = "system testing workflows"

content = """
Sistem testi iş akışları, tüm katmanların birlikte çalıştığı tam sistem davranışını
doğrular. Kullanıcı senaryoları, API zincirleri ve altyapı bileşenleri kapsanır.

**Bağlam:** Sistem testleri production'a en yakın ortamda çalışır. Deployment,
konfigürasyon ve ağ davranışı gerçek koşullara benzer şekilde test edilir.

**Temel prosedürler:**
1) Test ortamını production mimarisiyle uyumlu tutun; farklılıkları dokümante edin.
2) Kritik iş akışlarını önceliklendirin; risk tabanlı test seçimi yapın.
3) Test verilerini yönetin; production verisini kopyalamayın, sentetik veri kullanın.
4) Paralel çalıştırma için ortam izolasyonu sağlayın; paylaşılan durumdan kaçının.
5) Sonuçları merkezi raporlama sistemine gönderin; trend analizi yapın.

**Kabul kriterleri:** Sistem testleri haftalık veya release öncesi çalıştırılır,
tüm kritik akışlar kapsanır ve sonuçlar trace edilebilir olur.
"""  # noqa: E501

version = "0.0.1"
