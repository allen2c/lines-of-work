"""Onboarding flow for identity verification."""

title = "Flusso di onboarding e verifica identità"

content = """
Il flusso di onboarding per la verifica dell'identità segue una sequenza standard
che può variare in base al livello di rischio del cliente.

**Raccolta dati:** Nome, cognome, data di nascita, nazionalità, indirizzo.
Per persone giuridiche: dati societari, UBO, rappresentanti legali.

**Invio documenti:** Il cliente carica documento d'identità e prova di residenza.
Formati accettati: PDF, JPG, PNG. Dimensione massima e criteri di leggibilità.

**Verifica automatica:** OCR estrae dati, confronto con database, controllo
autenticità (ologrammi, microstampa). Esito: approvato, da revisione manuale,
o rifiutato.

**Video-identificazione (se richiesta):** Per EDD o quando la verifica automatica
non è sufficiente. Operatore qualificato o sistema automatizzato con liveness.

**Esito e retention:** Documenti e risultati conservati secondo normative. Il
cliente riceve conferma o richiesta di documentazione aggiuntiva.
"""  # noqa: E501

version = "0.0.1"
