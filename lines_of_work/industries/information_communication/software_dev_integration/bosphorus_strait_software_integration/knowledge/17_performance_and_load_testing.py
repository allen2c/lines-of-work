"""
Knowledge item 17: performance and load testing. Validates system behavior under
expected and peak load to prevent production degradation.
"""

title = "performance and load testing"

content = """
Performans ve yük testleri, sistemin beklenen ve zirve yük altındaki davranışını
doğrular; production'da yavaşlama veya çökme riskini önler. Yüksek trafikli
API servislerinde bu testler olmadan kapasite planlaması ve bottleneck tespiti
mümkün değildir.

**Bağlam:** Load testleri belirli eşzamanlı kullanıcı veya istek sayısı ile
sistemi zorlar; stress testleri sınırların ötesine iter. Latans, throughput,
hata oranı ve kaynak kullanımı ölçülür. Baseline oluşturulmalı ve regresyon
izlenmelidir.

**Temel prosedürler:**
1) Gerçekçi iş yükü profilleri tanımlayın (örn. kullanıcı sayısı, istek türleri, sıklık).
2) Kademeli yük artışı ile load testleri çalıştırın; kırılma noktasını belirleyin.
3) Latans percentillerini (p50, p95, p99) izleyin; SLA hedefleri ile karşılaştırın.
4) Bottleneck'leri (DB, ağ, CPU) tespit edin ve optimize edin.
5) Her major release öncesi performans regresyon testi yapın.

**Kabul kriterleri:** Performans testleri etkin when baseline kaydedilmiş, SLA
metrikleri tanımlı ve regresyon pipeline'da otomatik çalışıyor.

**Yaygın hatalar:** Test ortamının production'dan farklı olması; yanlış veya
eksik senaryolar. Azaltma: production-like ortam, gerçek veri anonimizasyonu.
"""  # noqa: E501

version = "0.0.1"
