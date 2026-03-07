"""
Knowledge item 15: end to end user flows. Validates complete user journeys from
entry point to outcome.
"""

title = "end to end user flows"

content = """
Uçtan uca kullanıcı akışları, bir kullanıcının sistemde gerçekleştirdiği tam
yolculuğu doğrular. Giriş noktasından (UI veya API) nihai sonuca kadar tüm
adımlar test edilir.

**Bağlam:** E2E testleri en yavaş ve en kırılgan test türüdür. Sadece en kritik
happy path ve alternatif akışlar için kullanılmalıdır.

**Temel prosedürler:**
1) Her release için 5-10 kritik kullanıcı senaryosu belirleyin; fazlası bakım yükü oluşturur.
2) Page Object veya benzeri desen kullanarak UI testlerini modüler tutun.
3) API tabanlı E2E tercih edin; UI testleri sadece gerekli yerlerde kullanın.
4) Retry ve timeout stratejisi tanımlayın; geçici ağ hatalarına karşı dayanıklı olun.
5) Test süresini izleyin; 30 dakikayı aşan suite'leri parçalayın.

**Kabul kriterleri:** E2E testleri haftalık çalışır, flaky oranı %5'in altındadır
ve başarısızlık durumunda net hata raporu üretir.
"""  # noqa: E501

version = "0.0.1"
