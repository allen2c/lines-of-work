"""
Knowledge item 20: security threat modeling. Identifies and mitigates security
risks in system design and integration points.
"""

title = "security threat modeling"

content = """
Güvenlik tehdit modellemesi, sistem tasarımı ve entegrasyon noktalarındaki
güvenlik risklerini tanımlar ve azaltır. STRIDE veya benzeri çerçeveler
kullanılarak spoofing, tampering, repudiation, bilgi ifşası, DoS ve privilege
escalation gibi tehditler değerlendirilir.

**Bağlam:** API'ler, veri akışları ve kimlik doğrulama noktaları tehdit
yüzeyini oluşturur. Erken tasarım aşamasında tehdit modellemesi yapmak,
sonradan pahalı düzeltmelerden kaçınmayı sağlar.

**Temel prosedürler:**
1) Sistem diyagramı çizin; veri akışları, güven sınırları ve varlıkları işaretleyin.
2) STRIDE ile her bileşen için tehditleri listeleyin.
3) Tehditleri risk skoruna göre önceliklendirin (olasılık x etki).
4) Her yüksek riskli tehdit için azaltma önlemi tanımlayın.
5) Büyük değişikliklerde tehdit modelini güncelleyin.

**Kabul kriterleri:** Tehdit modellemesi etkin when tüm kritik bileşenler
değerlendirilmiş, riskler dokümante ve azaltmalar uygulanmış.

**Yaygın hatalar:** Modelin güncel kalmaması; sadece teknik tehditlere odaklanma.
Azaltma: periyodik revizyon, iş ve uyumluluk risklerini dahil etme.
"""  # noqa: E501

version = "0.0.1"
