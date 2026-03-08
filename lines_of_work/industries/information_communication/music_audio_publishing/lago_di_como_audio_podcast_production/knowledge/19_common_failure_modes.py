"""Common failure modes and how to prevent or resolve them."""

title = "Modalità di guasto comuni e soluzioni"

content = """
Riconoscere i problemi ricorrenti permette di prevenirli e gestirli rapidamente quando si verificano.

**Release mancanti:** Ospite non ha firmato prima della registrazione. Soluzione: sospendere
pubblicazione fino a ricevere release. Implementare checklist pre-recording che blocca la sessione
se release non confermate.

**Livelli incoerenti:** Episodi con LUFS troppo basso o alto, o differenze tra voci. Soluzione:
template di mastering, verifica con meter prima dell'export. QC obbligatorio.

**Feed rotto:** URL enclosure non raggiungibile, SSL scaduto, hosting down. Soluzione: monitoring
regolare, alert su errori di validazione. Piano di backup per migrazione hosting.

**Ritardi nella catena:** Editing in ritardo blocca pubblicazione. Soluzione: buffer nel calendario,
comunicazione proattiva, escalation chiara ai responsabili.
"""  # noqa: E501

version = "0.0.1"
