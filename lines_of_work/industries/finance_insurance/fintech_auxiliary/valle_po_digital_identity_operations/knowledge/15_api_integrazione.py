"""API integration for identity verification."""

title = "Integrazione API per verifica identità"

content = """
L'API Valle Po permette ai clienti di integrare la verifica dell'identità nei
propri flussi senza intervento manuale.

**Autenticazione:** API key e secret per ambiente sandbox e produzione.
Header di autorizzazione su ogni richiesta. Rotazione chiavi consigliata.

**Endpoint principali:** Creazione sessione, upload documento, avvio video-ID,
consulta stato, recupera risultato. REST con JSON.

**Webhook:** Notifiche asincrone per cambio stato (pending, approved, rejected,
manual_review). Retry con backoff esponenziale in caso di failure.

**Rate limit:** Limiti per minuto e per giorno in base al piano. Codici 429
con header Retry-After. Per picchi, contattare il team commerciale.

**Ambiente sandbox:** Documenti di test predefiniti per simulare approvazione,
rifiuto e manual review. Non usare in produzione.
"""  # noqa: E501

version = "0.0.1"
