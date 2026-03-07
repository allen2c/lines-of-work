"""
Knowledge item 22: dark pools and alternative venues. Off-exchange trading
venues and their role in execution.
"""

title = "dark pool e venue alternativi"

content = """
I dark pool e i sistemi multilaterali di negoziazione (MTF) offrono alternative
alle borse tradizionali, con negoziazione anonima e spesso costi ridotti. La
desk deve bilanciare liquidità, trasparenza e best execution.

**Dark pool:** Mercati che non pubblicano ordini in book prima dell'esecuzione.
L'anonimato riduce il market impact per ordini di dimensione elevata. Tipi:
independent, broker-owned, exchange-operated. Liquidità variabile e frammentata.

**MTF (Multilateral Trading Facilities):** Sistemi di negoziazione regolamentati
che competono con le borse. Esempi: Turquoise, BATS Chi-X. Offrono latenza
ridotta e fee competitive. Ordini visibili nel book o in dark mode.

**Smart order routing:** Instradare ordini verso i venue ottimali in base a
liquidità, costi, probabilità di fill e istruzioni del cliente. Evitare
information leakage attraverso l'ordine flow.

**Regolamentazione:** MiFID II impone trasparenza pre e post-trade, limiti
per dark pool (double volume cap), e reporting. Rispettare i volumi ammessi
per negoziazione in dark.

**Trade-off:** I dark pool possono offrire migliori prezzi e minore impact,
ma con liquidità incerta e rischio di information leakage. Valutare caso per
caso in base a dimensione, urgenza e caratteristiche del titolo.
"""  # noqa: E501

version = "0.0.1"
