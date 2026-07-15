title = "Monitoraggio e gestione dei posti letto"

content = """
- Ogni mattina alle 7:00, il sistema genera il report dei posti letto occupati, liberi, in attesa di dimissione.
- I posti letto sono classificati per reparto, tipologia (ordinario, DH, TI, subintensiva) e stato (libero, occupato, in sanificazione).
- Il tasso di occupazione target è 85-90%; se supera il 95%, attivare alert e comunicare alla Direzione Sanitaria.
- I letti in sanificazione devono essere pronti entro 2 ore dalla dimissione; se il tempo supera le 3 ore, segnalare alle pulizie.
- Per i ricoveri programmati, bloccare i letti nel sistema 24 ore prima; se il paziente non arriva, sbloccare dopo 1 ora.
"""

version = "0.0.1"
