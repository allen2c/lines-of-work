"""
Knowledge item 13: fixed income trading. Core mechanics of bond and fixed income
instrument trading for the desk.
"""

title = "trading titoli a reddito fisso"

content = """
Il trading di titoli a reddito fisso comprende obbligazioni governative, corporate,
titoli garantiti da ipoteca e strumenti del mercato monetario. A differenza delle
azioni, i titoli a reddito fisso negoziano spesso over-the-counter (OTC) con
market maker che quotano bid/ask, piuttosto che su borse centralizzate.

**Struttura del mercato:** I titoli di Stato (BTP, Bund, Treasury) sono i più
liquidi. Le obbligazioni corporate hanno spread di credito che riflettono il
rischio di default. I titoli garantiti da ipoteca (MBS) presentano complessità
aggiuntive legate al prepayment e alla struttura dei flussi.

**Quotazione:** I titoli sono quotati in prezzo (percentuale del valore nominale)
o in yield. La relazione prezzo-rendimento è inversa: quando i tassi salgono, i
prezzi scendono. La duration misura la sensibilità del prezzo alle variazioni
dei tassi.

**Liquidità:** La liquidità varia significativamente tra emissioni. I titoli
on-the-run (più recenti) sono più liquidi degli off-the-run. I blocchi di grandi
dimensioni richiedono spesso negoziazione bilaterale o aste.

**Settlement:** Il regolamento dei titoli di Stato italiani avviene tipicamente
T+2 tramite Monte Titoli. I titoli internazionali possono richiedere custodi
locali e regolamento in valuta estera.

**Rischio di credito:** Lo spread rispetto al titolo di Stato di riferimento
(benchmark) compensa il rischio di default. I rating delle agenzie (Moody's,
S&P, Fitch) influenzano la domanda e i requisiti di margine.

**Corporate actions:** Le obbligazioni possono avere call, put, conversioni e
eventi di default. La gestione corretta richiede monitoraggio delle scadenze
e delle clausole contrattuali.
"""  # noqa: E501

version = "0.0.1"
