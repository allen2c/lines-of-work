"""
Knowledge item 20: performance measurement. Metrics and benchmarks for evaluating
execution quality and trading desk effectiveness.
"""

title = "misurazione prestazioni"

content = """
La misurazione delle prestazioni di esecuzione valuta la qualità del servizio
offerto dalla desk di negoziazione. Gli indicatori principali includono il
costo di implementazione, lo slippage, il market impact e il fill rate.

**Implementation shortfall:** Differenza tra il prezzo di decisione (quando il
cliente decide di negoziare) e il prezzo di esecuzione effettivo, al netto dei
costi espliciti. Misura il costo totale dell'esecuzione inclusi timing e
market impact. Obiettivo: minimizzare lo shortfall rispetto al benchmark.

**VWAP/TWAP benchmark:** Confrontare l'esecuzione con il volume-weighted
average price o time-weighted average price del periodo. Utile per ordini
distribuiti nel tempo. Considerare le limitazioni: VWAP favorisce esecuzioni
in periodi ad alto volume.

**Arrival price:** Prezzo di mercato al momento dell'arrivo dell'ordine.
Benchmark comune per ordini singoli. Lo shortfall rispetto all'arrival price
cattura timing e market impact.

**Fill rate:** Percentuale dell'ordine eseguita entro il timeframe richiesto.
Ordini parziali o non eseguiti riducono il fill rate. Monitorare per ordini
urgenti o con vincoli temporali stringenti.

**Slippage:** Differenza tra prezzo atteso e prezzo effettivo. Può essere
positivo (miglioramento) o negativo (peggioramento). Analizzare per dimensione
ordine, liquidità e condizioni di mercato.

**Reportistica:** Fornire report periodici ai clienti con metriche di esecuzione,
confronti con benchmark e analisi per asset class e tipo di ordine.
"""  # noqa: E501

version = "0.0.1"
