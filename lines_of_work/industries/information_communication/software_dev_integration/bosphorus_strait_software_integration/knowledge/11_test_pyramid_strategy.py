"""
Knowledge item 11: test pyramid strategy. Defines unit, integration, and E2E test ratios
for balanced coverage and fast feedback.
"""

title = "test pyramid strategy"

content = """
Test piramidi stratejisi, birim testlerinin tabanda, entegrasyon testlerinin ortada ve
uçtan uca testlerin tepede olduğu bir dağılım öngörür. Bu dağılım hızlı geri bildirim
ve maliyet-etkin kapsam sağlar.

**Bağlam:** Dağıtık API ortamlarında çok sayıda birim testi hızlı çalışır; az sayıda
E2E testi yavaş ama gerçek senaryoları doğrular. Piramit oranları (ör. 70-20-10) risk
ve süre dengesine göre ayarlanmalıdır.

**Temel prosedürler:**
1) Kritik iş mantığı için birim testleri yazın; mock kullanarak izolasyon sağlayın.
2) Servisler arası sözleşmeler ve veri akışları için entegrasyon testleri ekleyin.
3) E2E testleri sadece kritik kullanıcı akışları için sınırlı tutun.
4) Piramit oranlarını periyodik olarak gözden geçirin; flaky testleri azaltın.
5) CI pipeline süresini izleyin; gereksiz yavaş testleri optimize edin.

**Kabul kriterleri:** Piramit etkin sayılır when birim testleri dakikalar içinde,
entegrasyon testleri on dakikalar içinde, E2E testleri yarım saat içinde tamamlanır.
"""  # noqa: E501

version = "0.0.1"
