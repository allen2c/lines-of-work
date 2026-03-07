"""Webhook security and validation."""

title = "Sicurezza e validazione webhook"

content = """
I webhook Valle Po sono firmati (HMAC) per verifica autenticità. Header
X-Signature contiene firma; clienti devono validare prima di elaborare.
Retry automatici per failure 4xx/5xx con backoff esponenziale. Endpoint
deve rispondere 200 entro 30 secondi. Documentazione include esempi
validazione in vari linguaggi.
"""  # noqa: E501

version = "0.0.1"
