"""
Knowledge item 06: algorithmic trading strategies and execution algorithms.
"""

title = "Algoritmi di esecuzione"

content = """
Gli algoritmi di esecuzione suddividono ordini di grandi dimensioni in componenti più
piccole, eseguite nel tempo per minimizzare l'impatto di mercato e ottimizzare il
prezzo medio di esecuzione rispetto a benchmark definiti.

**VWAP (Volume-Weighted Average Price)** mira a eseguire al prezzo medio ponderato per
il volume dell'intera giornata. L'algoritmo stima la curva di volume e distribuisce
l'ordine di conseguenza. Efficace quando l'obiettivo è allinearsi al mercato.

**TWAP (Time-Weighted Average Price)** distribuisce l'ordine uniformemente nel tempo,
indipendente dal volume. Utile per ordini che non vogliono seguire i pattern di volume
o quando la stima del volume è incerta.

**Implementation shortfall** minimizza la differenza tra il prezzo di decisione e il
prezzo di esecuzione effettivo, bilanciando rischio di mercato e impatto. Adatto quando
la priorità è minimizzare il costo totale di esecuzione.

**POV (Percentage of Volume)** esegue una percentuale fissa del volume di mercato,
adattandosi dinamicamente alla liquidità. Riduce il rischio di information leakage.

**Iceberg** mostra solo una frazione dell'ordine nel book, nascondendo la dimensione
totale. Utile per ordini grandi in titoli con book poco profondi.

**Parametri critici** includono aggressività, orizzonte temporale, limiti di prezzo e
condizioni di stop. La calibrazione richiede backtest e monitoraggio continuo.
"""  # noqa: E501

version = "0.0.1"
