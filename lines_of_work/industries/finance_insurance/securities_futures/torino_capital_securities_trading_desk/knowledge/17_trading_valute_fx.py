"""
Knowledge item 17: FX and currency trading. Foreign exchange mechanics for
the securities desk.
"""

title = "trading valute e FX"

content = """
Il trading FX supporta le operazioni in titoli denominati in valute diverse e
la gestione del rischio di cambio per portafogli internazionali. La desk può
eseguire FX spot, forward e swap in supporto alle attività principali.

**Coppie di valute:** Le coppie maggiori (EUR/USD, USD/JPY, GBP/USD) hanno
liquidità elevata e spread stretti. Le coppie emergenti e incrociate hanno
spread più ampi. La convenzione di quotazione (base/quote) deve essere
compresa per evitare errori.

**Spot e forward:** Lo spot si regola tipicamente T+2. I forward fissano un
tasso per una data futura, utili per hedging. Gli NDF (non-deliverable forward)
si regolano in contanti per valute con restrizioni.

**Swap FX:** Gli swap combinano spot e forward in direzioni opposte, utilizzati
per roll di posizioni e per il funding in valuta estera.

**Settlement:** Il rischio di Herstatt (settlement risk) sorge quando una parte
effettua il pagamento prima di ricevere la contropartita. I meccanismi di
payment-versus-payment (PvP) riducono questo rischio.

**Orari di mercato:** Il mercato FX opera 24 ore durante la settimana lavorativa,
con sessioni asiatica, europea e americana. La liquidità varia per sessione.
"""  # noqa: E501

version = "0.0.1"
