"""RSS feed structure and requirements for podcast distribution."""

title = "Struttura del feed RSS per podcast"

content = """
Il feed RSS è il canale attraverso cui le piattaforme (Spotify, Apple Podcasts, ecc.) recuperano
episodi e metadati. Un feed malformato impedisce l'approvazione o aggiornamenti corretti.

**Elementi obbligatori:** channel (title, link, description, language), item per ogni episodio con
enclosure (URL audio, type MIME, length in bytes). La data di pubblicazione (pubDate) deve essere RFC 2822.

**Best practice:** Utilizzare tag iTunes (itunes:author, itunes:image, itunes:explicit) e
podcast: namespace per migliorare la compatibilità. L'immagine del canale: minimo 1400x1400 px,
formato quadrato, JPG o PNG.

**Validazione:** Verificare il feed con il validatore Apple Podcasts o Podbase prima della submit.
Errori comuni: enclosure mancanti, URL audio non raggiungibili, date incoerenti.
"""  # noqa: E501

version = "0.0.1"
