"""Sandbox environment for integration testing."""

title = "Sandbox e Testing Integrazione"

content = """
L'ambiente sandbox permette di testare l'integrazione senza processare
verifiche reali.

**Credenziali:** API key separate per sandbox e produzione. Non usare
chiavi di produzione in test.

**Documenti di test:** forniamo documenti campione (carta identità, passaporto)
che simulano esiti approved, failed, manual_review. Usarli per validare
tutti i percorsi del flusso.

**Rate limiting:** limiti più permissivi in sandbox per agevolare test
automatizzati.

**Webhook:** endpoint di test riceve gli stessi payload di produzione
per validare la gestione degli eventi.
"""  # noqa: E501

version = "0.0.1"
