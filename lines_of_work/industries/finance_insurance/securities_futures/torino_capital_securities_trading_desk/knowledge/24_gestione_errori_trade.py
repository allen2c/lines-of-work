"""
Knowledge item 24: trade error handling. Procedures for identifying, resolving
and preventing execution errors.
"""

title = "gestione errori di negoziazione"

content = """
Gli errori di negoziazione (trade errors) possono derivare da input errati,
malfunzionamenti di sistema o misinterpretazione delle istruzioni. Una
gestione rapida e strutturata minimizza perdite e rischi reputazionali.

**Classificazione:** Errori di prezzo (esecuzione a prezzo errato), di
dimensione (quantità errata), di titolo (strumento sbagliato), di lato
(acquisto invece di vendita) o di controparte. Ogni tipo richiede procedure
specifiche di risoluzione.

**Rilevamento:** Controlli intraday su esecuzioni anomale: prezzi fuori
dallo spread abituale, dimensioni inattese, orari insoliti. Recon end-of-day
tra ordini, esecuzioni e posizioni. Alert automatici per soglie predefinite.

**Risoluzione immediata:** Per errori rilevati in tempo reale, valutare
l'annullamento o la correzione con la controparte o il venue. Per errori
su mercati regolamentati, seguire le procedure di annullamento dell'exchange.

**Allocazione:** Se l'errore riguarda l'allocazione a conti clienti,
correggere l'allocazione e trasferire le posizioni. Documentare la
correzione e le motivazioni.

**Break resolution:** Per differenze tra i nostri registri e quelli della
controparte o del custode, investigare la causa, conciliare e risolvere.
Escalation se la break persiste oltre i termini concordati.

**Prevenzione:** Doppio controllo per ordini di dimensione elevata,
validazione automatica di prezzo e quantità, formazione periodica,
review post-mortem degli errori per migliorare i processi.
"""  # noqa: E501

version = "0.0.1"
