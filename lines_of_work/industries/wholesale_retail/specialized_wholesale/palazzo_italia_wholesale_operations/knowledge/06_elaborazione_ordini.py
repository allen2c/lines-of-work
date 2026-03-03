title = "Elaborazione ordini cliente"

content = """
Il processo di elaborazione ordini segue un flusso standard: ricezione, verifica, allocazione,
picking, imballaggio e spedizione.

**Ricezione ordine:**
Gli ordini possono arrivare via email, portale B2B, EDI o telefono. Vanno registrati in
ERP con tutti i riferimenti: cliente, articoli, quantità, prezzo, termini di consegna.

**Verifica:**
- Disponibilità stock
- Rispetto MOQ (minimo d'ordine) per articolo o brand
- Limite di credito del cliente
- Coerenza con listini e politiche commerciali

**Allocazione e picking:**
Lo stock disponibile viene allocato all'ordine. Il picking list guida il magazziniere.
Eventuali mancanze vengono segnalate; il cliente va avvisato e l'ordine parzialmente evaso
o posticipato secondo politiche.
"""

version = "0.0.1"
