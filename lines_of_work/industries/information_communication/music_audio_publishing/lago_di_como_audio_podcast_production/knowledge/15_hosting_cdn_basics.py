"""Hosting and CDN basics for podcast distribution."""

title = "Nozioni base su hosting e CDN per podcast"

content = """
L'hosting del feed e degli file audio deve garantire disponibilità e velocità. Un server instabile
o lento danneggia l'esperienza e il posizionamento sulle piattaforme.

**Requisiti:** Server con supporto HTTPS, bandwidth sufficiente per il traffico atteso. RSS e file
audio devono essere serviti con MIME type corretti. SSL valido (certificato non scaduto).

**CDN:** Per podcast con ascolti elevati, un CDN riduce la latenza e distribuisce il carico.
Provider specializzati (Libsyn, Buzzsprout, Transistor) includono hosting, analytics e integrazione
con le piattaforme.

**Manutenzione:** Monitorare uptime e tempi di risposta. Pianificare rinnovi e backup. In caso di
migrazione, gestire redirect e aggiornamento URL nel feed.
"""  # noqa: E501

version = "0.0.1"
