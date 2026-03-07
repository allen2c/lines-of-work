"""Retry policy and resubmission procedures."""

title = "Politica di retry e risottomissione"

content = """
**Retry automatici:** L'API supporta retry automatici per errori temporanei (timeout,
rate limit, indisponibilità). Il client deve implementare backoff esponenziale con
massimo 3 tentativi per richiesta.

**Risottomissione documenti:** Se la verifica fallisce per qualità immagine o
documento illeggibile, il cliente può risottomettere. Massimo 2 risottomissioni
per sessione. Dopo 2 fallimenti, è richiesta video-identificazione o documento
alternativo.

**Cooldown:** Dopo 5 tentativi falliti in 15 minuti, l'endpoint applica un cooldown
di 30 minuti. Contattare il supporto per sblocco anticipato in casi legittimi.

**Idempotenza:** Usare lo stesso idempotency key per retry della stessa richiesta.
Evitare duplicati.
"""  # noqa: E501

version = "0.0.1"
