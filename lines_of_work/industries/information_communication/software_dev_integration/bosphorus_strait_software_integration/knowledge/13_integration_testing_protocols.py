"""
Knowledge item 13: integration testing protocols. Covers service-to-service and
database integration test design.
"""

title = "integration testing protocols"

content = """
Entegrasyon test protokolleri, birden fazla bileşenin birlikte çalışmasını doğrulayan
testlerin tasarım ve yürütme kurallarını tanımlar. Gerçek veya test konteynerleri
kullanılabilir.

**Bağlam:** Dağıtık sistemlerde servisler arası iletişim, veritabanı işlemleri ve
mesaj kuyrukları entegrasyon testleriyle doğrulanmalıdır. Test ortamı production'a
yakın olmalı ancak izole kalmalıdır.

**Temel prosedürler:**
1) Test veritabanını her test sınıfı veya suite başında sıfırlayın; veri sızıntısını önleyin.
2) Harici servisler için WireMock veya benzeri stub kullanın; gerçek API'lara bağlanmayın.
3) Timeout değerlerini makul tutun; takılı testler pipeline'ı bloke etmesin.
4) Test sırasını belirleyin; paralel çalıştırma için izolasyon sağlayın.
5) Başarısızlık durumunda yeterli log ve trace toplayın; hata ayıklamayı kolaylaştırın.

**Kabul kriterleri:** Entegrasyon testleri tekrarlanabilir, bağımsız ve 15 dakika
içinde tamamlanabilir olmalıdır.
"""  # noqa: E501

version = "0.0.1"
