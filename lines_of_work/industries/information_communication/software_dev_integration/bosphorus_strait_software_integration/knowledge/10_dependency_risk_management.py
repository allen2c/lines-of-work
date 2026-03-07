"""
Knowledge item 10: dependency risk management. Identifies and mitigates risks
from third-party and internal dependencies.
"""

title = "dependency risk management"

content = """
Bağımlılık risk yönetimi, üçüncü taraf ve dahili bağımlılıklardan kaynaklanan
riskleri belirler ve azaltır. Harici paketler, API'ler ve altyapı servisleri
kontrol dışı değişikliklere ve güvenlik açıklarına maruz kalabilir.

**Bağlam:** Bosphorus Strait projeleri npm, pip, Maven ve harici API'ler kullanır.
Her bağımlılık güncellemesi veya kesintisi iş süreçlerini etkileyebilir.

**Temel prosedürler:**
1) Tüm bağımlılıkları envantere alın; lisans, sürüm ve kritiklik derecesi ekleyin.
2) Güvenlik taraması otomatikleştirin; CVE uyarıları için Dependabot veya benzeri kullanın.
3) Majör güncellemelerde kırılma riski değerlendirin; sandbox ortamda test edin.
4) Kritik harici API'ler için yedek sağlayıcı veya fallback stratejisi planlayın.
5) Bağımlılık güncelleme politikası tanımlayın; yama süreleri belirleyin.

**Kabul kriterleri:** Envanter güncel, güvenlik taraması çalışıyor ve kritik
bağımlılıklar için azaltma planı mevcut olduğunda etkin sayılır.
"""  # noqa: E501

version = "0.0.1"
