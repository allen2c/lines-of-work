title = "Gestione SLA e tempi di risposta"

content = """
- SLA di risposta: P1=1h, P2=2h, P3=4h, P4=8h (ore lavorative 8-18, lun-ven). SLA di risoluzione: P1=4h, P2=8h, P3=24h, P4=72h.
- Monitora il timer SLA nel sistema. Se un ticket si avvicina al 70% del tempo di risoluzione senza progressi, avvia escalation.
- Per P1, invia un aggiornamento ogni 30 minuti fino alla risoluzione. Per P2 ogni ora, P3 ogni 2 ore, P4 ogni 4 ore.
- Se il ticket supera il 100% del tempo SLA, notifica automaticamente il service manager e registra una non conformità.
"""  # noqa: E501

version = "0.0.1"
