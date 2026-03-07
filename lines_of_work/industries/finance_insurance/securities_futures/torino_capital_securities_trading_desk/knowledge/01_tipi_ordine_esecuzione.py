"""
Knowledge item 01: order types and execution methods for securities trading.
"""

title = "Tipi di ordine e metodi di esecuzione"

content = """
I tipi di ordine e i metodi di esecuzione costituiscono la base del trading di titoli,
determinando come, quando e a quale prezzo le operazioni verranno eseguite. La comprensione
di questi meccanismi è essenziale per ottimizzare la qualità dell'esecuzione e gestire
i costi di transazione.

**Ordini a mercato** rappresentano l'istruzione di esecuzione più basilare, dirigendo i
broker ad acquistare o vendere titoli immediatamente al miglior prezzo disponibile. Questi
ordini privilegiano la velocità rispetto alla certezza del prezzo, ideali per titoli
altamente liquidi dove l'impatto sul prezzo è minimo. In mercati volatili, gli ordini a
mercato possono causare slippage dove il prezzo di esecuzione differisce significativamente
dal prezzo quotato al momento dell'inserimento.

**Ordini limite** specificano un prezzo massimo di acquisto o minimo di vendita, fornendo
protezione sul prezzo ma nessuna garanzia di esecuzione. Gli ordini restano nel book fino
al raggiungimento del prezzo o alla scadenza. Le condizioni time-in-force determinano la
durata: day order, good-till-cancelled (GTC), immediate-or-cancel (IOC).

**Ordini stop** attivano ordini a mercato al raggiungimento di un livello di prezzo,
comunemente usati per mitigazione delle perdite o strategie momentum. Gli stop-loss
proteggono i profitti limitando le perdite vendendo automaticamente quando i prezzi
scendono sotto un livello predeterminato.

**Algoritmi di esecuzione** hanno rivoluzionato il trading istituzionale suddividendo ordini
grandi in componenti più piccole eseguite nel tempo. VWAP mira alla media ponderata per
volume; TWAP distribuisce l'esecuzione uniformemente; implementation shortfall minimizza
l'impatto di mercato adattando il ritmo dinamicamente.

**Smart order routing** indirizza automaticamente gli ordini al venue ottimale in base a
liquidità, costi, velocità e opportunità di price improvement.
"""  # noqa: E501

version = "0.0.1"
