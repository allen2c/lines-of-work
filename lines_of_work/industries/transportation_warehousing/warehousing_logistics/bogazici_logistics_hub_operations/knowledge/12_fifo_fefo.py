title = "FIFO ve FEFO Stok Yönetimi"

content = """
FIFO (İlk Giren İlk Çıkar) ve FEFO (İlk Biten İlk Çıkar) stok rotasyon
stratejileridir. Son kullanma tarihi olan ürünlerde FEFO tercih edilir.

**FIFO Uygulaması:** Aynı SKU için birden fazla parti varsa, en eski
lot numarası önce sevk edilir. Depo yerleşimi ve WMS konum kodu bunu
desteklemelidir.

**FEFO Uygulaması:** Gıda, ilaç veya kozmetik gibi raf ömrü kısıtlı
ürünlerde son kullanma tarihi baz alınır. En yakın tarih önceliklidir.

**Boğaziçi Uygulaması:** Avrupa-Asya transit yüklerinde karışık ürün
profili nedeniyle her SKU için rotasyon kuralı WMS'de tanımlıdır.
"""  # noqa: E501

version = "0.0.1"
