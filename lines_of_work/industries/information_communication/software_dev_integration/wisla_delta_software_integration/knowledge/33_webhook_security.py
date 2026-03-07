title = "Bezpieczeństwo webhooków"

content = """
Webhooki dostarczają dane do zewnętrznych URL-i. Bez zabezpieczeń są podatne na
fałszerstwo i ataki. Kluczowe mechanizmy:

**Podpis HMAC:** Serwer podpisuje payload kluczem współdzielonym. Odbiorca weryfikuje
podpis przed przetworzeniem. Nagłówek X-Webhook-Signature lub podobny.

**Weryfikacja TLS:** Zawsze HTTPS. Certyfikaty muszą być ważne. Unikać samopodpisanych
w produkcji.

**Idempotency key:** Zapobiega wielokrotnemu przetwarzaniu tego samego zdarzenia
przy retry. Odbiorca śledzi przetworzone identyfikatory.
"""  # noqa: E501

version = "0.0.1"
