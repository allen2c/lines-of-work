"""
Knowledge item 07: API contract design. Defines stable, versioned interfaces for
service integration.
"""

title = "api contract design"

content = """
API sözleşme tasarımı, servis entegrasyonları için kararlı ve sürümlü arayüzler
tanımlar. İyi tasarlanmış sözleşmeler, taraflar arasındaki beklentileri netleştirir
ve geriye dönük uyumluluk bozulmalarını önler.

**Bağlam:** Dağıtık mimarilerde her servis kendi API'sini sunar. Sözleşmeler
OpenAPI, GraphQL şeması veya protobuf ile belgelenmeli; değişiklikler sürüm
stratejisine uygun yapılmalıdır.

**Temel prosedürler:**
1) Request/response şemalarını, hata kodlarını ve zorunlu alanları açıkça tanımlayın.
2) Sürümleme stratejisi belirleyin: URL tabanlı (/v1/, /v2/) veya header tabanlı.
3) Geriye dönük uyumluluk kurallarını belgeleyin; alan ekleme izinli, kaldırma yasak.
4) Sözleşme testleri ile tüketici ve sağlayıcı tarafını doğrulayın.
5) Kullanım dışı (deprecation) süreçlerini tanımlayın; en az bir yayın döngüsü bildirim.

**Kabul kriterleri:** Sözleşmeler merkezi depoda tutuluyor, CI'da doğrulanıyor ve
tüm tüketiciler bilgilendirildiğinde etkin sayılır.
"""  # noqa: E501

version = "0.0.1"
