"""
Knowledge item 03: risk management frameworks for trading desks.
"""

title = "Framework di gestione del rischio"

content = """
I framework di gestione del rischio per le trading desk definiscono limiti, metriche e
procedure per contenere l'esposizione a perdite e garantire la stabilità operativa.
Consob, Banca d'Italia e norme MiFID II impongono requisiti stringenti.

**Limiti di posizione** definiscono il massimo esposizione consentita per singolo titolo,
settore, o controparte. I limiti devono essere calibrati in base al capitale, alla
liquidità e al profilo di rischio dell'istituzione.

**Value at Risk (VaR)** stima la perdita massima attesa entro un orizzonte temporale e un
livello di confidenza. VaR parametrico, storico e Monte Carlo offrono approcci diversi;
nessuno cattura completamente il tail risk.

**Stress testing** valuta l'impatto di scenari estremi (crolli di mercato, default di
controparte) sul portafoglio. I test devono includere eventi storici e scenari ipotetici
rilevanti per il profilo dell'istituzione.

**Limiti di prenotazione** (pre-trade) bloccano ordini che eccederebbero i limiti di
rischio. I controlli devono essere automatizzati e in tempo reale per essere efficaci.

**Concentration risk** emerge quando posizioni eccessive in singoli titoli o settori
amplificano le perdite. I limiti di concentrazione mitigano questo rischio.

**Operational risk** include errori di esecuzione, guasti di sistema, frode. Procedure
di riconciliazione, doppio controllo e audit trail sono essenziali.
"""  # noqa: E501

version = "0.0.1"
