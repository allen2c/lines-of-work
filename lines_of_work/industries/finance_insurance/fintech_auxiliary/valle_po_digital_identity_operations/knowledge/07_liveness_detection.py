"""Liveness detection and anti-spoofing."""

title = "Liveness Detection e Anti-Spoofing"

content = """
Il liveness detection assicura che la persona sia presente in tempo reale, non
una foto, video o maschera.

**Metodi passivi:** Analisi della texture della pelle, riflessi, profondità.
Eseguibili senza azione esplicita dell'utente.

**Metodi attivi:** L'utente esegue un gesto (sorriso, girare la testa, battere
le palpebre). Maggiore sicurezza, possibile impatto su UX.

**Anti-spoofing:** Rilevamento di foto stampate, schermi, maschere 3D. I
fornitori aggiornano continuamente i modelli contro nuovi attacchi.

**Conformità:** Il liveness è richiesto da molte linee guida per verifica remota
di identità. eIDAS e normativa italiana riconoscono liveness come elemento di
sicurezza.

**Fallimenti:** Illuminazione estrema, occhiali con riflessi, movimenti troppo
veloci possono causare retry. Guidare l'utente con messaggi chiari.
"""  # noqa: E501

version = "0.0.1"
