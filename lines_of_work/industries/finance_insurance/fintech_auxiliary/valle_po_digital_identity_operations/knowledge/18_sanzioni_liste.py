"""Sanctions lists and screening."""

title = "Liste di sanzioni e screening"

content = """
Lo screening contro le liste di sanzioni è obbligatorio per tutti i soggetti
obbligati AML. Nessuna transazione o relazione con soggetti sanzionati.

**Liste principali:** UE (consolidata), OFAC (USA), ONU, liste nazionali (es.
Italia). Alcuni clienti richiedono anche liste aggiuntive (es. settore export).

**Match:** Confronto fuzzy su nome, data di nascita, nazionalità. I falsi
positivi sono frequenti (nomi comuni). La risoluzione manuale verifica se il
match è un vero positivo.

**False positive:** Stesso nome ma persona diversa. Documentazione della
verifica e motivazione del falso positivo conservata per audit.

**True positive:** Blocco immediato. Nessuna relazione commerciale. Segnalazione
all'UIF se richiesto dalla normativa. Non informare il soggetto della segnalazione.
"""  # noqa: E501

version = "0.0.1"
