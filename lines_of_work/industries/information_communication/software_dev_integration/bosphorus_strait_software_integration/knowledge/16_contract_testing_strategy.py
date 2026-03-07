"""
Knowledge item 16: contract testing strategy. Ensures API consumers and providers
stay compatible through explicit contract definitions and automated verification.
"""

title = "contract testing strategy"

content = """
Sözleşme testleri, API tüketicileri ve sağlayıcıları arasındaki uyumluluğu, açık
sözleşme tanımları ve otomatik doğrulama ile garanti eder. Dağıtık sistemlerde
her servis bağımsız deploy edildiğinde, sözleşme ihlalleri production'da hata
üretir; bu testler bu riski önceden yakalar.

**Bağlam:** OpenAPI, GraphQL şeması veya Pact gibi araçlarla sözleşmeler tanımlanır.
Consumer-driven contract testleri tüketici beklentilerini sözleşme olarak kaydeder;
provider testleri bu sözleşmeleri karşıladığını doğrular. Her iki taraf da CI/CD
pipeline'ında çalıştırılmalıdır.

**Temel prosedürler:**
1) Her kritik API için sözleşme formatını seçin (OpenAPI, Pact, vb.) ve versiyonlama
   stratejisi belirleyin.
2) Consumer tarafında beklenen request/response örneklerini sözleşme olarak dışa aktarın.
3) Provider tarafında sözleşme testlerini her build'de çalıştırın; uyumsuzlukta build kırılsın.
4) Breaking change'lerde sürüm artırın ve tüm tüketicileri bilgilendirin.
5) Sözleşme testlerini gerçek entegrasyon testlerinden ayırın; sözleşme hızlı ve izole olmalı.

**Kabul kriterleri:** Sözleşme testleri etkin sayılır when tüm kritik API'ler sözleşme
ile tanımlı, CI'da otomatik çalışıyor ve breaking change'ler dokümante edilmiş.

**Yaygın hatalar:** Sözleşmelerin çok gevşek veya çok katı olması; provider'ın
gerçek davranışı ile sözleşmenin uyuşmaması. Azaltma: düzenli sözleşme revizyonu,
örnek veri kullanımı ve canlı API ile karşılaştırma.
"""  # noqa: E501

version = "0.0.1"
