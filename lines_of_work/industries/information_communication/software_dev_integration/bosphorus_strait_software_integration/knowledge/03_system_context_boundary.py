"""
Knowledge item 03: system context boundary. Defines what is in scope and out of scope
for the system under test to avoid scope creep and unclear ownership.
"""

title = "system context boundary"

content = """
Sistem bağlam sınırı, test edilen sistemin kapsamını ve kapsam dışını tanımlar.
Belirsiz sınırlar, sorumluluk boşluklarına ve entegrasyon hatalarına yol açar.

**Bağlam:** Bosphorus Strait entegrasyonları birden fazla harici sistemle konuşur.
Her entegrasyonun sınırları, veri sahipliği ve hata sorumluluğu net olmalıdır.

**Temel prosedürler:**
1) Sistem bağlam diyagramı çizin; dahil ve hariç tutulan bileşenleri işaretleyin.
2) Her sınır geçişinde veri formatı, protokol ve hata davranışını tanımlayın.
3) Üçüncü taraf sistemler için sorumluluk matrisi oluşturun; kim neyi garanti eder?
4) Mock ve stub kullanımını sınırlara göre planlayın; hangi bileşenler gerçek, hangisi simüle?
5) Sınır değişikliklerini değişiklik yönetimiyle takip edin.

**Kabul kriterleri:** Bağlam sınırı tanımlı sayılır when diyagram onaylanmış, tüm
arayüzler dokümante edilmiş ve sorumluluk matrisi paydaşlarca kabul edilmiştir.

**Yaygın hatalar:** Sınırları çok geniş tutmak; harici bağımlılıkları görmezden gelmek.
Azaltma: minimal viable boundary ile başlayın, gerektikçe genişletin.
"""  # noqa: E501

version = "0.0.1"
