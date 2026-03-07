"""Post-release monitoring practices."""

title = "Monitoring After Release"

content = """
Na elke release moet monitoring actief zijn. Definieer key metrics: error rates, latency
percentiles, throughput, en business KPIs. Stel alerting in met realistische drempels
gebaseerd op baseline. Plan een post-release observatieperiode (bijv. 30–60 minuten)
waarin het team beschikbaar is. Correlatie met deployment-timestamp helpt bij
root cause analyse. Log aggregatie en distributed tracing moeten operationeel zijn
voordat de release start.
"""

version = "0.0.1"
