"""Gestione eccezioni nel workflow di verifica."""

title = "Gestione Eccezioni nel Workflow"

content = """
Eccezioni comuni: documenti non supportati, qualità insufficiente, timeout
liveness, errori di rete. Ogni eccezione ha un codice e una procedura.

**Documento non supportato:** Verificare lista documenti accettati per paese.
Se il documento è valido ma non in lista, escalation a Product per valutazione.

**Qualità insufficiente:** Guidare l'utente a rifotografare con luce adeguata,
evitando riflessi. Non accettare screenshot o foto di foto.

**Timeout:** Retry automatico se configurabile. Altrimenti, nuovo tentativo
da parte dell'utente. Verificare latenza di rete se ricorrente.
"""  # noqa: E501

version = "0.0.1"
