"""Monitoring and alerts knowledge for Lyon Forge developer experience."""

title = "Monitoring et alertes en développement"

content = """
Les développeurs Lyon Forge ont accès aux dashboards de monitoring des environnements
de staging et de développement. Comprendre ces outils aide à diagnostiquer les problèmes
avant la production.

**Métriques clés:** Latence, taux d'erreur, débit. Les métriques business (conversions,
transactions) sont aussi disponibles pour les environnements de test.

**Alertes:** En développement, les alertes sont configurées avec des seuils plus permissifs
qu'en production. Les faux positifs fréquents indiquent un besoin d'ajuster les seuils ou
d'améliorer la stabilité des environnements de test.

**Corrélation:** Lors d'un bug, croiser les logs, les traces et les métriques. Les
timestamps doivent être en UTC. Les identifiants de requête permettent de suivre un
flux à travers les services.
"""

version = "0.0.1"
