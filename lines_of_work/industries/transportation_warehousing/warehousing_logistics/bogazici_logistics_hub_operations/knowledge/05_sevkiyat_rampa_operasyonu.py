title = "Sevkiyat ve Rampa Operasyonu"

content = """
Sevkiyat rampası, paketlerin kargo firmalarına teslim edildiği noktadır.
Boğaziçi Hub'da günlük sevkiyat dalgaları sabah, öğle ve akşam olmak üzere
üç vardiyada planlanır.

**Dalga Planlaması:** Siparişler kargo firması ve varış bölgesine göre
gruplanır. Öncelik express ve aynı gün teslimat siparişlerine verilir.

**Rampa Yükleme:** Paletler ve koli grupları kargo aracına rota sırasına
göre yüklenir. Son varış noktası en önde olacak şekilde (LIFO) yerleştirilir.

**Teslim Protokolü:** Sürücü manifestoyu imzalar; paket sayısı ve ağırlık
kaydedilir. Eksik veya hasarlı paket tespiti anında raporlanır.

**Takip Numarası:** Her sevkiyat için takip numarası üretilir; müşteri
bildirimi otomatik yapılır.
"""  # noqa: E501

version = "0.0.1"
