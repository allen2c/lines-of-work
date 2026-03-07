"""
Knowledge item 10: position management. Tracking and reconciling trading positions.
"""

title = "gestione delle posizioni"

content = """
La gestione delle posizioni garantisce accuratezza tra libri contabili, controparti
e sistemi di clearing. Errori non corretti generano rischio operativo e regolamentare.

**Position reconciliation** confronta posizioni tra front-office, middle-office,
custodi e clearing house. Le differenze devono essere investigate e risolte daily.

**Settlement positions** tracciano titoli in attesa di regolamento (pending), fails
e partial deliveries. Il follow-up sui fail riduce rischio di controparte e costi.

**Corporate actions** richiedono aggiornamento delle posizioni per dividendi, split,
fusioni e offerte. La mancata elaborazione causa errori di posizione e perdite.

**Multi-venue aggregation** consolida posizioni da più borse, dark pool e OTC in
una vista unificata per rischio e P&L.

**Position limits** devono essere monitorati in tempo reale. I breach attivano blocchi
e escalation.

**Segregation** tra posizioni proprie e clienti è obbligatoria. La commingling viola
normative e espone a sanzioni.
"""  # noqa: E501

version = "0.0.1"
