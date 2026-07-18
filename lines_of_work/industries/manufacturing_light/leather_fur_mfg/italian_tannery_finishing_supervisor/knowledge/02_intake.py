title = "Ricezione e Identificazione Lotti"

content = """
- All’arrivo dal reparto asciugatura, ogni lotto riceve etichetta RFID con: ID lotto, articolo, spessore target, colore Pantone, quantità (mq).
- Verifica visiva: assenza di pieghe, muffe, contaminazioni; fotografare e archiviare in MES.
- Controllo documentale: scheda tecnica cliente (ST‑CLI‑xxx) e scheda interna (SI‑FIN‑yyy) devono coincidere.
- Registrazione timestamp ingresso (UTC+1) e assegnazione a linea spruzzatura in base a priorità (cliente, scadenza).
- Soglia di accettazione ingresso: umidità pelle 12‑14 % (misurato con igrometro a contatto); fuori range → segnalazione a qualità.
"""  # noqa: E501

version = "0.0.1"
