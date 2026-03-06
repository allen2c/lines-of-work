title = "Stok Optimizasyonu"

content = """
Stok optimizasyonu, talep tahmini ile tedarik sürelerini dengeleyerek hem
eksik stok hem de aşırı stok riskini minimize eder. Boğaziçi Lojistik Hub
Avrupa-Asya transit trafiğinde hızlı devir hedefler.

**ABC Analizi:** A sınıfı ürünler (yüksek değer, düşük hacim) sık sayım ve
güvenlik stoku ile takip edilir. C sınıfı ürünler daha az kaynak tüketir.

**Güvenlik Stoku:** Tedarik süresi belirsizliği ve talep dalgalanmasına göre
hesaplanır. Transit gecikmeleri İstanbul trafiğinde dikkate alınmalıdır.

**Yeniden Sipariş Noktası:** Ortalama tüketim × tedarik süresi + güvenlik stoku.
WMS otomatik uyarı verecek şekilde yapılandırılmalıdır.
"""  # noqa: E501

version = "0.0.1"
