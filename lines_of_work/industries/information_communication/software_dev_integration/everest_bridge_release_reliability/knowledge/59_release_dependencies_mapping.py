"""Release dependencies mapping."""

title = "Release Dependencies Mapping"

content = """
Releases hebben vaak dependencies: andere services, libraries, of infrastructuur. Map deze
expliciet om verrassingen en deployment volgorde problemen te voorkomen.

**Service dependencies:** Welke services moeten eerst of tegelijk gedeployed worden? API
contract wijzigingen: welke consumers moeten meebewegen? Documenteer in release plan.

**Infra dependencies:** Database migrations, config changes, nieuwe secrets. Volgorde en
compatibiliteit zijn kritiek. Backward compatibility voorkomt big-bang deployments.

**Communicatie:** Bij gedeelde dependencies: coördineer met eigenaars. Dependency graph
visualisatie helpt bij release planning.
"""

version = "0.0.1"
