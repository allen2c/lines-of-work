"""
Knowledge item 05: quality attributes definition. Defines measurable quality attributes
such as availability, latency, and correctness for the system.
"""

title = "quality attributes definition"

content = """
Kalite nitelikleri tanımı, sistem için kullanılabilirlik, gecikme ve doğruluk gibi
ölçülebilir nitelikleri tanımlar. Ölçülemeyen hedefler yönetilemez.

**Bağlam:** Bosphorus Strait hizmetleri yüksek trafik ve düşük gecikme gerektirir.
Kalite nitelikleri SLO/SLA ile uyumlu olmalı ve iş hedefleriyle bağlantılı olmalıdır.

**Temel prosedürler:**
1) İş kritikliğine göre nitelikleri önceliklendirin: availability, latency, throughput, correctness.
2) Her nitelik için ölçüm yöntemi ve hedef değer tanımlayın.
3) Trade-off'ları dokümante edin; örn. düşük latency vs. yüksek throughput.
4) Nitelikleri test stratejisine bağlayın; hangi test hangi niteliği doğrular?
5) Nitelikleri dashboards ve alerting ile izleyin.

**Kabul kriterleri:** Nitelikler tanımlı sayılır when ölçülebilir, hedefler sayısal
ve test stratejisiyle eşleşmiştir.

**Yaygın hatalar:** Çok fazla nitelik; ölçülemeyen hedefler. Azaltma: 5-7 temel
nitelikle başlayın, SMART kriterleri kullanın.
"""  # noqa: E501

version = "0.0.1"
