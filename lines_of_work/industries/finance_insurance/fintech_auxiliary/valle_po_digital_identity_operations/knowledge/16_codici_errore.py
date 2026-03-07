"""Error codes and troubleshooting."""

title = "Codici errore e risoluzione problemi"

content = """
I codici errore API e le cause comuni aiutano a risolvere rapidamente i problemi
di integrazione.

**DOCUMENT_UNREADABLE:** Immagine sfocata, riflessi, angolazione errata.
Soluzione: chiedere al cliente di riprendere con luce adeguata, documento piatto.

**DOCUMENT_EXPIRED:** Documento scaduto. Non accettabile per KYC. Richiedere
documento valido.

**FACE_MISMATCH:** Il volto nella foto documento non corrisponde al selfie.
Possibile frode o errore di acquisizione. Revisione manuale o nuovo tentativo.

**LIVENESS_FAILED:** Il controllo liveness non è superato (foto di foto, video).
Richiedere nuovo tentativo con istruzioni chiare.

**RATE_LIMIT_EXCEEDED:** Troppe richieste. Attendere e ritentare. Verificare
implementazione retry.

**INVALID_API_KEY:** Chiave errata o revocata. Controllare ambiente e credenziali.
"""  # noqa: E501

version = "0.0.1"
