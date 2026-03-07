"""Comunicazione dei rifiuti al cliente."""

title = "Comunicazione dei Rifiuti al Cliente"

content = """
Quando una verifica fallisce, il messaggio al cliente deve essere chiaro ma non
rivelare dettagli che potrebbero aiutare frodatori a correggere i tentativi.

**Cosa comunicare:** Indicare che la verifica non è andata a buon fine e
suggerire azioni (es. controllare qualità foto, documenti non scaduti). Non
specificare quale controllo ha fallito (es. liveness, MRZ, face match).

**Retry:** Informare se è possibile riprovare e con quali limiti. Evitare
messaggi generici che frustrano l'utente senza dare indicazioni utili.

**Supporto:** Fornire canale di contatto per casi legittimi (documenti danneggiati,
problemi tecnici). Il supporto può richiedere documentazione aggiuntiva.
"""  # noqa: E501

version = "0.0.1"
