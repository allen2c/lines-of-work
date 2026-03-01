title = "Tracciabilità inventario e codici"

content = """
Ogni articolo in magazzino è identificato da codici univoci che consentono tracciabilità dal
fornitore al cliente finale.

**Struttura codici:**
- Codice articolo: composto da prefisso brand, riferimento collezione e variante
- Codice lotto/ricevuta: legato alla singola reception dal fornitore
- Ubicazione: identificativo fisico della posizione in magazzino

**Sistema di tracciabilità:**
L'ERP registra ogni movimentazione (entrata, uscita, trasferimento, rettifica). Le query per
lotto o articolo permettono di risalire a ricevimenti, ordini clienti e spedizioni associate.

**Requisiti Made in Italy:**
Per i brand con certificazione di origine, la tracciabilità deve dimostrare la filiera produttiva.
I documenti di accompagnamento del fornitore sono conservati e collegati al lotto.
"""

version = "0.0.1"
