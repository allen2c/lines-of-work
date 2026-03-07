"""Automated document verification process."""

title = "Verifica Documentale Automatizzata"

content = """
La verifica documentale automatizzata (ADV) confronta il documento caricato con
modelli noti e controlla elementi di sicurezza.

**Estrazione dati:** OCR estrae nome, cognome, data di nascita, numero documento,
scadenza. I dati vengono confrontati con quanto dichiarato dal cliente.

**Controlli di autenticità:** Verifica ologrammi, microstampa, font ufficiali.
Documenti falsi o alterati vengono segnalati per revisione manuale.

**Liveness e matching:** In flussi con selfie, il volto viene confrontato con
la foto sul documento. Il liveness assicura che non sia una foto di una foto.

**Esiti:** Approvato (verifica completata), Rifiutato (documento non valido),
Revisione manuale (dubbio, richiede operatore). I tempi medi sono sotto i 60 secondi.

**Limitazioni:** Documenti molto danneggiati, illuminazione scarsa o angolazioni
estreme possono richiedere nuovo upload o passaggio a video-identificazione.
"""  # noqa: E501

version = "0.0.1"
