"""Release go/no-go decision criteria."""

title = "Release Go/No-Go Criteria"

content = """
Go/no-go meetings bepalen of een release doorgang vindt. Criteria moeten vooraf gedefinieerd,
meetbaar en bindend zijn. Geen release zonder expliciete go.

**Technische criteria:** Alle tests groen, geen open P0/P1 bugs in scope, staging verificatie
geslaagd, rollback procedure getest. Security en compliance checks afgerond.

**Organisatorische criteria:** Release notes klaar, stakeholders geïnformeerd, support voorbereid.
Geen conflicterende deployments van andere teams in hetzelfde venster.

**Besluit:** Eén persoon (Release Manager) heeft finale stem. Bij twijfel: no-go. Documenteer
reden bij no-go voor leerpunten.
"""

version = "0.0.1"
