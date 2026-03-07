title = "Szyfrowanie danych w tranzycie"

content = """
Dane przesyłane między systemami muszą być chronione. TLS (HTTPS) jest standardem dla
komunikacji sieciowej. Używaj TLS 1.2 lub nowszego; wyłącz starsze protokoły.

**Certyfikaty:** Weryfikuj certyfikaty serwera. W środowiskach wewnętrznych używaj
zaufanych CA. Nigdy nie pomijaj weryfikacji w produkcji.

**Klucze:** Rotuj klucze API i tokeny zgodnie z polityką bezpieczeństwa.
"""  # noqa: E501

version = "0.0.1"
