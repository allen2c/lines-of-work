"""
Knowledge item 12: derivatives trading mechanics. Options, futures, and structured products.
"""

title = "meccanica dei derivati"

content = """
I derivati (opzioni, futures, swap) richiedono conoscenza di pricing, margini e
clearing specifici. Il desk deve gestire greci, scadenze e controparti.

**Opzioni** conferiscono il diritto (non obbligo) di comprare (call) o vendere (put)
il sottostante a uno strike entro la scadenza. Il premio dipende da volatilità,
tempo e tassi. Le strategie combinate (spread, straddle) gestiscono rischio e costo.

**Futures** sono contratti standardizzati per consegna futura. Margini giornalieri
(mark-to-market) richiedono liquidità. Il roll su contratti successivi mantiene
l'esposizione.

**Swap** (IRS, CDS, equity swap) sono OTC e richiedono CSA per collateral. Il
valuation e il margine variano per controparte.

**Clearing** per derivati standardizzati passa da CCP (central counterparty). Il
margine iniziale e variazionale proteggono dalla controparte.

**Corporate actions** su sottostanti (dividendi, split) influenzano opzioni e
futures. Le adjustment devono essere applicate correttamente.
"""  # noqa: E501

version = "0.0.1"
