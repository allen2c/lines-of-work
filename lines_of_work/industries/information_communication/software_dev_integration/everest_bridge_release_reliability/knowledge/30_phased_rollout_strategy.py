"""Phased rollout approach."""

title = "Phased Rollout Strategy"

content = """
Phased rollouts beperken risico door wijzigingen geleidelijk uit te rollen. De typische
fasering: 1) interne of canary groep, 2) klein percentage productiegebruikers,
3) grotere gebruikersgroep, 4) volledige uitrol.

**Fase-overgangscriteria:** Definieer meetbare criteria om naar de volgende fase te gaan:
geen kritieke bugs, metrics binnen acceptabele bandbreedte, en geen escalaties. Gebruik
feature flags of traffic splitting om verkeer te sturen. Houd per fase een rollback
optie open.

**Documentatie:** Documenteer het rollout plan in de release documentatie. Vermeld
verwachte duur per fase, verantwoordelijken, en beslismomenten. Communiceer
vooruitgang naar stakeholders.
"""

version = "0.0.1"
