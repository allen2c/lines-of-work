"""
Knowledge item 21: ETF trading. Mechanics and considerations for trading
exchange-traded funds.
"""

title = "trading ETF"

content = """
Gli ETF (Exchange-Traded Funds) combinano caratteristiche di fondi comuni e
azioni, negoziando in borsa con prezzi in tempo reale. La desk deve gestire
creazione/rimborso, arbitraggio NAV-premium e liquidità primaria/secondaria.

**Struttura:** Gli ETF replicano indici o panieri mediante replica fisica
(totale o campionata) o sintetica (swap). Il market maker e gli AP
(Authorized Participants) creano e rimborsano quote in blocchi (creation units).

**Liquidità:** La liquidità primaria deriva dal mercato sottostante; quella
secondaria dalle negoziazioni in borsa. Per ETF poco liquidi, verificare lo
spread bid-ask e la profondità prima di eseguire ordini di dimensione elevata.

**Premium/discount:** Il prezzo di mercato può discostarsi dal NAV. Un premium
indica domanda elevata; uno sconto può segnalare illiquidità o timori. Per
ordini grandi, considerare la creazione/rimborso diretta con l'emittente.

**Orari di negoziazione:** Gli ETF azionari seguono gli orari di borsa. Il NAV
viene calcolato a chiusura. Durante la giornata, il prezzo riflette le
aspettative sul NAV di chiusura.

**Costi:** Commissioni di negoziazione, spread bid-ask e, per creazione/
rimborso, costi di transazione sul paniere. Confrontare il costo di acquisto
in borsa con quello di creazione per ordini di dimensioni significative.

**Corporate actions:** Dividendi e frazionamenti influenzano il prezzo e il
NAV. Verificare le date ex e di stacco per una corretta pianificazione.
"""  # noqa: E501

version = "0.0.1"
