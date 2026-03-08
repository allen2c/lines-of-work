"""LUFS (Loudness Units Full Scale) standards for podcast audio."""

title = "Standard LUFS per podcast"

content = """
Gli standard LUFS definiscono il livello di loudness target per garantire omogeneità tra episodi e
conformità alle piattaforme. Un livello incoerente affatica l'ascoltatore e riduce la qualità percepita.

**Target -16 LUFS:** Lo standard de facto per podcast parlati. Spotify e Apple Podcasts normalizzano
intorno a -14 LUFS, ma -16 LUFS per contenuti parlati riduce la compressionione eccessiva e mantiene
dinamica naturale. Adattare il target in base alle specifiche del cliente.

**Misurazione:** Utilizzare un meter integrated (short-term o momentary) durante il mastering.
Verificare che l'intero episodio rispetti il target; i picchi isolati non devono superare -1 dBTP.

**Range dinamico:** Per interviste e narrative, una dinamica moderata (6–10 dB) migliora l'esperienza.
Evitare livellamento aggressivo che appiattisce la voce.
"""  # noqa: E501

version = "0.0.1"
