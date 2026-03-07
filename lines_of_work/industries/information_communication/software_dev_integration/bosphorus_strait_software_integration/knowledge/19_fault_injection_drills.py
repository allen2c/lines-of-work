"""
Knowledge item 19: fault injection drills. Proactively tests system behavior
under failure conditions to validate resilience.
"""

title = "fault injection drills"

content = """
Hata enjeksiyon tatbikatları, sistemin hata koşulları altındaki davranışını
proaktif olarak test eder. Chaos engineering prensipleriyle, production'a
benzer ortamda kasıtlı hatalar tetiklenir; sistemin dayanıklılığı ve
kurtarma süreçleri doğrulanır.

**Bağlam:** Ağ gecikmesi, servis kesintisi, yüksek CPU veya bellek baskısı
gibi senaryolar simüle edilir. Amaç, gizli tek nokta arızalarını ve yanlış
hata varsayımlarını ortaya çıkarmaktır. Tatbikatlar kontrollü ve izole
ortamda yapılmalıdır.

**Temel prosedürler:**
1) Blast radius'u sınırlayın; önce staging veya canary ortamında deneyin.
2) Senaryoları önceden tanımlayın: hangi bileşen, ne tür hata, ne kadar süre.
3) Gözlemleme ve metrik toplama hazır olsun; tatbikat sırasında davranışı kaydedin.
4) Post-mortem yapın; bulguları dokümante edin ve iyileştirme planı oluşturun.
5) Düzenli tatbikat takvimi belirleyin (örn. aylık).

**Kabul kriterleri:** Hata enjeksiyonu etkin when senaryolar dokümante, blast
radius kontrol altında ve iyileştirmeler uygulanmış.

**Yaygın hatalar:** Production'da kontrolsüz chaos; yetersiz gözlemleme.
Azaltma: game days, runbook'lar ve on-call hazırlığı.
"""  # noqa: E501

version = "0.0.1"
