"""
Knowledge item 12: unit testing standards. Defines isolation, naming, and coverage
expectations for unit tests.
"""

title = "unit testing standards"

content = """
Birim test standartları, tek bir fonksiyon veya sınıfın davranışını izole ortamda
doğrulayan testlerin yazım kurallarını tanımlar. Dış bağımlılıklar mock veya stub
ile değiştirilir.

**Bağlam:** Birim testleri hızlı, deterministik ve bakımı kolay olmalıdır. Gerçek
veritabanı, ağ veya dosya sistemine bağlanmamalıdır.

**Temel prosedürler:**
1) Arrange-Act-Assert (AAA) desenini kullanın; her test tek bir senaryoyu kapsasın.
2) Açıklayıcı isimlendirme: test_<method>_<condition>_<expected_result>.
3) Coverage hedefi: kritik iş mantığı için %80+; tüm satırlar için değil.
4) Flaky testlere tolerans göstermeyin; zaman veya rastgelelik bağımlılıklarını kaldırın.
5) Test verilerini fabrika veya fixture ile yönetin; hardcode'dan kaçının.

**Kabul kriterleri:** Birim testleri 5 saniyeden kısa sürede çalışır, CI'da yeşil
kalır ve değişiklik yapıldığında anlamlı hata mesajları verir.
"""  # noqa: E501

version = "0.0.1"
