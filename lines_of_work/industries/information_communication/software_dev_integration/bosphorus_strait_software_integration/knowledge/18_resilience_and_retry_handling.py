"""
Knowledge item 18: resilience and retry handling. Designs retry, backoff, and
circuit breaker patterns for fault-tolerant integrations.
"""

title = "resilience and retry handling"

content = """
Dayanıklılık ve yeniden deneme mekanizmaları, geçici hatalara karşı sistemin
kendini toparlamasını sağlar. Retry, exponential backoff ve circuit breaker
desenleri, dağıtık entegrasyonlarda kritik öneme sahiptir; yanlış uygulama
ise cascade failure veya thundering herd'e yol açar.

**Bağlam:** Geçici ağ hataları, zaman aşımı veya yoğunluk nedeniyle başarısız
olan istekler, kontrollü yeniden deneme ile başarılı olabilir. Ancak sürekli
başarısız bir servise retry yapmak kaynakları tüketir; circuit breaker bu
durumda devreyi açar ve hızlı başarısızlık döner.

**Temel prosedürler:**
1) Idempotent işlemler için retry kullanın; non-idempotent işlemlerde dikkatli olun.
2) Exponential backoff ile retry aralığını artırın; jitter ekleyin.
3) Maksimum retry sayısı ve toplam timeout belirleyin.
4) Circuit breaker: failure threshold aşıldığında açık, belirli süre sonra yarı-açık test.
5) Fallback veya graceful degradation stratejisi tanımlayın.

**Kabul kriterleri:** Dayanıklılık etkin when retry/backoff parametreleri
dokümante, circuit breaker konfigüre ve fallback test edilmiş.

**Yaygın hatalar:** Retry'da infinite loop; circuit breaker'ın çok erken veya
geç açılması. Azaltma: metrik izleme, chaos testleri ile doğrulama.
"""  # noqa: E501

version = "0.0.1"
