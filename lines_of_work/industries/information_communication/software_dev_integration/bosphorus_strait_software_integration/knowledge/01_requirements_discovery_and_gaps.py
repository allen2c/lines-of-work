"""
Knowledge item 01: requirements discovery and gaps. Identifies missing or ambiguous
requirements that could affect reliability before development starts.
"""

title = "requirements discovery and gaps"

content = """
Gereksinim keşfi ve boşluk analizi, geliştirme başlamadan önce eksik veya belirsiz
gereksinimleri tespit eder. Bu süreç olmadan, güvenilirlik riskleri geç keşfedilir
ve düzeltme maliyeti katlanır.

**Bağlam:** Avrupa-Asya köprüsü konumundaki Bosphorus Strait, çok dilli ve çok
bölgeli entegrasyonlarla çalışır. Gereksinim boşlukları özellikle sınır ötesi
veri akışları, zaman dilimi ve uyumluluk senaryolarında ortaya çıkar.

**Temel prosedürler:**
1) Paydaşlarla workshop'lar düzenleyerek iş hedeflerini ve başarı kriterlerini netleştirin.
2) Mevcut dokümantasyonu tarayarak eksik senaryoları, edge case'leri ve NFR'leri listeleyin.
3) Risk tabanlı önceliklendirme yapın; yüksek etkili akışlar için detaylı gereksinim toplayın.
4) Kabul kriterlerini ölçülebilir ve test edilebilir şekilde tanımlayın.
5) Boşlukları raporlayın ve sahiplik atayın; kritik boşluklar çözülmeden geliştirmeye geçmeyin.

**Kabul kriterleri:** Gereksinim keşfi tamamlanmış sayılır; tüm kritik akışlar
dokümante edilmiş, belirsizlikler işaretlenmiş ve en az bir paydaş onayı alınmıştır.

**Yaygın hatalar:** Sadece mutlu yol senaryolarını toplamak; NFR'leri ertelemek;
paydaş katılımını yetersiz tutmak. Azaltma: checklist kullanın, cross-functional
review yapın ve iteratif geri bildirim alın.
"""  # noqa: E501

version = "0.0.1"
