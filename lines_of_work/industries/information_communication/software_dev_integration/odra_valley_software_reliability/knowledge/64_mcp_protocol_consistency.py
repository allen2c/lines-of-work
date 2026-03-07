"""Knowledge item: mcp protocol consistency."""

title = "Spójność protokołu MCP"

content = """
Model Context Protocol (MCP) definiuje standardową warstwę komunikacji między agentami a
zewnętrznymi narzędziami. Zespół niezawodności weryfikuje, że implementacje MCP są zgodne
ze specyfikacją i zachowują się przewidywalnie pod obciążeniem.

**Kontekst:** Niezgodności protokołu prowadzą do błędów integracji, utraty kontekstu lub
awarii w łańcuchach wywołań. Testy muszą obejmować wersjonowanie, retry i obsługę błędów.

**Kluczowe działania:**
1) Weryfikuj zgodność z oficjalną specyfikacją MCP.
2) Testuj scenariusze timeout, niepowodzenia i częściowe odpowiedzi.
3) Sprawdzaj idempotencję operacji przy retry.
4) Udokumentuj obsługiwane wersje i ograniczenia.
"""

version = "0.0.1"
