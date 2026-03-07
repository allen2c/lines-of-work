"""Webhook notifications for verification status updates."""

title = "Webhook e Notifiche di Stato"

content = """
I webhook notificano i clienti quando lo stato di una verifica cambia.

**Eventi supportati:** verification.completed, verification.failed,
verification.pending_review, verification.expired.

**Payload:** JSON con verification_id, status, timestamp, e dettagli
opzionali (reason_code, retry_count). Firma HMAC per autenticità.

**Retry policy:** fino a 5 tentativi con backoff esponenziale (1m, 5m,
15m, 1h, 4h). Dopo fallimento, il cliente deve interrogare l'API per
lo stato attuale.

**Configurazione:** URL webhook configurato nel portale partner. Supporto
per endpoint di test (sandbox) e produzione. Verificare certificato SSL.
"""  # noqa: E501

version = "0.0.1"
