"""Zero downtime deployment strategies."""

title = "Zero Downtime Deployment"

content = """
Zero-downtime deployments vermijden onderbreking van service tijdens releases. Strategieën:
rolling updates, blue-green, of canary. Kies op basis van infrastructuur en risicotolerantie.

**Rolling:** Oude instances worden één voor één vervangen door nieuwe. Geen extra capaciteit
nodig. Risico: tijdelijke mixed versions tijdens rollout.

**Blue-green:** Volledige parallelle omgeving. Switch verkeer in één keer. Snel rollback
door switch terug. Vereist dubbele capaciteit tijdens switch.

**Canary:** Klein percentage verkeer naar nieuwe versie. Vergelijk metrics, scale up of
rollback. Minimale impact bij problemen. Meer complexiteit in routing.
"""

version = "0.0.1"
