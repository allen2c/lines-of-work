"""
Knowledge item 08: domain model validation. Ensures business rules and invariants
hold across integration boundaries.
"""

title = "domain model validation"

content = """
Alan modeli doğrulama, iş kurallarının ve değişmezlerin entegrasyon sınırları
boyunca korunduğundan emin olur. Dağıtık sistemlerde her servis kendi modeline
sahiptir; sınırlarda dönüşüm ve doğrulama kritiktir.

**Bağlam:** Bosphorus Strait projelerinde alan modelleri sınırlı bağlamlar (bounded
context) ile tanımlanır. Paylaşılan kernel ve müşteri-tedarikçi ilişkileri net
sözleşmelerle yönetilir.

**Temel prosedürler:**
1) Her sınırlı bağlam için varlıklar, değer nesneleri ve agregatları belgeleyin.
2) Sınır geçişlerinde dönüşüm kurallarını tanımlayın; veri kaybı veya anlam
   bozulması kabul edilemez.
3) İş kuralı ihlallerini tespit etmek için birim ve entegrasyon testleri yazın.
4) Harici sistemlerden gelen verileri güvenilmez kabul edin; giriş doğrulama zorunlu.
5) Model değişikliklerinde etki analizi yapın; tüm tüketicileri güncelleyin.

**Kabul kriterleri:** Modeller belgelenmiş, sınır dönüşümleri test edilmiş ve
değişiklik yönetimi tanımlı olduğunda etkin sayılır.
"""  # noqa: E501

version = "0.0.1"
