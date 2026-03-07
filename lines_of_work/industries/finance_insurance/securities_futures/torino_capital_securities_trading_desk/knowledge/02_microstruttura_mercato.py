"""
Knowledge item 02: market microstructure and venue analysis.
"""

title = "Microstruttura del mercato"

content = """
La microstruttura del mercato studia i processi e i meccanismi attraverso cui gli ordini
si trasformano in transazioni. La comprensione della microstruttura è fondamentale per
ottimizzare l'esecuzione e valutare la qualità dei diversi venue di trading.

**Book di ordini** rappresenta la raccolta di ordini buy e sell in attesa di esecuzione.
La profondità del book indica la liquidità disponibile a diversi livelli di prezzo. I
market maker e gli specialisti forniscono liquidità continuativa, quotando bid e ask.

**Spread bid-ask** misura il costo immediato di transazione: la differenza tra il miglior
prezzo di vendita e il miglior prezzo di acquisto. Spread più stretti indicano maggiore
liquidità e minori costi di transazione per gli investitori.

**Venue di trading** includono borse regolamentate (Borsa Italiana, Xetra), dark pool per
negoziazione anonima, e sistemi multilaterali di negoziazione (MTF). Ogni venue presenta
caratteristiche di liquidità, trasparenza e costi diverse.

**Fragmentation** descrive la distribuzione del volume tra più venue. La frammentazione
offre opportunità di price improvement ma richiede smart order routing efficace per
raggiungere best execution.

**Tick size** definisce l'incremento minimo di prezzo consentito. Regolamenti come MiFID II
hanno introdotto tick size harmonizzati per migliorare la trasparenza e la liquidità.

**Pre-trade trasparenza** riguarda la visibilità delle quotazioni prima dell'esecuzione;
**post-trade trasparenza** riguarda la pubblicazione delle transazioni. Entrambe influenzano
la discovery del prezzo e la qualità dell'esecuzione.
"""  # noqa: E501

version = "0.0.1"
